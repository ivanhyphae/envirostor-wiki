#!/usr/bin/env python3
"""Compare sage-wiki summarize: DeepSeek V4 Flash vs Gemini 2.5 Flash."""

import json, os, textwrap, urllib.request, re

DOC_PATH = "wiki/pdf2md/RDIP Variance Request Acceptance E-Mail/RDIP Variance Request Acceptance E-Mail.md"
doc_text = open(DOC_PATH).read()

# Read keys from config.yaml
cfg = open("config.yaml").read()
m_or = re.search(r'api_key:\s*(sk-or-\S+)', cfg)
m_oa = re.search(r'embed:\n\s+api_key:\s*(sk-proj-\S+)', cfg, re.MULTILINE | re.DOTALL)
OPENROUTER_KEY = m_or.group(1) if m_or else ""
OPENAI_KEY = m_oa.group(1) if m_oa else ""

# Gemini key from env (only safe place to keep it)
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")

PROMPT = textwrap.dedent(f"""\
You are a technical writer creating a structured summary of an environmental 
remediation document for a wiki knowledge base.

**Document:** RDIP Variance Request Acceptance E-Mail

**Source text:**
{doc_text}

Please produce a concise, structured summary covering:
1. **Title**
2. **Key Parties**
3. **Purpose**
4. **Key Findings/Decisions**
5. **Implications**

Format as plain markdown with section headers.
""")

def call_openrouter(model, prompt):
    data = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
    }).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=data,
        headers={"Authorization": f"Bearer {OPENROUTER_KEY}", "Content-Type": "application/json"},
    )
    resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
    content = resp["choices"][0]["message"]["content"]
    usage = resp.get("usage", {})
    return content, usage

def call_gemini(model, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}"
    data = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 2000},
    }).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
    content = resp["candidates"][0]["content"]["parts"][0]["text"]
    usage = resp.get("usageMetadata", {})
    return content, usage

print("=" * 70)
print("MODEL COMPARISON: RDIP Variance Request Acceptance E-Mail")
print("=" * 70)

# DeepSeek V4 Flash
print("\n--- DEEPSEEK V4 FLASH ---")
result_ds, usage_ds = call_openrouter("deepseek/deepseek-v4-flash", PROMPT)
print(result_ds)
print(f"Tokens: {usage_ds.get('prompt_tokens','?')} in / {usage_ds.get('completion_tokens','?')} out")

# Gemini 2.5 Flash
print("\n--- GEMINI 2.5 FLASH ---")
result_gm, usage_gm = call_gemini("gemini-2.5-flash", PROMPT)
print(result_gm)
print(f"Tokens: {usage_gm.get('promptTokenCount','?')} in / {usage_gm.get('candidatesTokenCount','?')} out")

in_ds = usage_ds.get("prompt_tokens", 0) or 0
out_ds = usage_ds.get("completion_tokens", 0) or 0
in_gm = usage_gm.get("promptTokenCount", 0) or usage_gm.get("prompt_tokens", 0) or 0
out_gm = usage_gm.get("candidatesTokenCount", 0) or usage_gm.get("completion_tokens", 0) or 0

print("\n" + "=" * 70)
print("COST COMPARISON  (both ~$0.15/M in, $0.60/M out)")
print("=" * 70)
print(f"  DeepSeek V4 Flash:  {in_ds:>5} in / {out_ds:>5} out  ${(in_ds/1e6*0.15 + out_ds/1e6*0.60):.6f}")
print(f"  Gemini 2.5 Flash:   {in_gm:>5} in / {out_gm:>5} out  ${(in_gm/1e6*0.15 + out_gm/1e6*0.60):.6f}")
