"""
Table integrity guard for wiki compilation.

Prevents misaligned markdown tables from corrupting LLM downstream processing.
Provides validation, filtering, and optional repair heuristics.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple

# Critical files with severe table corruption — exclude from LLM processing
EXCLUDE_FROM_LLM_TABLES = [
    "Draft Interim RACR_ App D-G.md",  # 186 cells per line, 235 table blocks; unmanageable
    "S9800-01-17 Modesto Stockpiles June 2014 GW Mon 0814.md",  # 24 cells, 198 blocks, inconsistent
]

# High-risk files with >10 columns — process with caution
HIGH_RISK_WIDE_TABLES = [
    "06A2542ct_TO97_GW Rpt_final.20230308.md",  # Consolidated 2006-2023 GW data
    "7453_S9525-06-44_Modesto_Stockpiles_July_2012_GW_Report.1112.md",  # July 2012 GW
    "S1200-01-01 Modesto Stockpiles GW April 2019_06.19.md",  # Final GW round
]

def should_process_tables_in_file(filename: str) -> bool:
    """
    Determine if markdown tables in this file should be passed to LLM.

    Returns False if file is known to have corrupt/unmanageable tables.
    Use in wiki compilation pipeline to skip poisoned table blocks.
    """
    return not any(excluded in filename for excluded in EXCLUDE_FROM_LLM_TABLES)


def is_high_risk_file(filename: str) -> bool:
    """Mark files with wide tables (>10 columns) for manual review."""
    return any(risk in filename for risk in HIGH_RISK_WIDE_TABLES)


def extract_table_blocks(lines: List[str]) -> List[Dict]:
    """
    Extract potential markdown table blocks from a list of lines.

    A table block is a sequence of consecutive lines containing pipes (|).
    Returns list of dicts with metadata for each block.
    """
    blocks = []
    current_block = []
    block_start = None

    for i, line in enumerate(lines):
        pipe_count = line.count('|')

        if pipe_count >= 2:  # At least 2 pipes = potential table
            if not current_block:
                block_start = i
            current_block.append({'line_num': i, 'content': line, 'pipe_count': pipe_count})
        else:
            # End of block
            if current_block:
                blocks.append({
                    'start_line': block_start,
                    'end_line': i - 1,
                    'line_count': len(current_block),
                    'rows': current_block,
                })
                current_block = []
                block_start = None

    # Don't forget last block
    if current_block:
        blocks.append({
            'start_line': block_start,
            'end_line': len(lines) - 1,
            'line_count': len(current_block),
            'rows': current_block,
        })

    return blocks


def validate_table_block(rows: List[Dict], tolerance: int = 2) -> Tuple[bool, Dict]:
    """
    Validate a table block for structural integrity.

    Args:
        rows: List of row dicts with 'pipe_count' and 'content'
        tolerance: Allow cell count variance up to this many cells

    Returns:
        (is_valid, diagnostics) tuple
    """
    if not rows:
        return False, {'reason': 'empty block'}

    # Expected cell count from first data row (skip separator row if present)
    cell_counts = [max(0, r['pipe_count'] - 1) for r in rows]

    # Skip separator rows (all dashes and pipes)
    data_cell_counts = []
    for count, row in zip(cell_counts, rows):
        if not re.match(r'^[\|\s\-:]+$', row['content']):
            data_cell_counts.append(count)

    if not data_cell_counts:
        return False, {'reason': 'no data rows (all separator)'}

    expected_count = data_cell_counts[0]
    variance = max(data_cell_counts) - min(data_cell_counts)

    # Check consistency
    corrupted_rows = []
    for i, (count, row) in enumerate(zip(data_cell_counts, rows)):
        if abs(count - expected_count) > tolerance:
            corrupted_rows.append({
                'row_index': i,
                'line_number': row['line_num'],
                'expected_cells': expected_count,
                'actual_cells': count,
            })

    is_valid = variance <= tolerance and not corrupted_rows

    diagnostics = {
        'total_rows': len(rows),
        'expected_cells': expected_count,
        'min_cells': min(data_cell_counts) if data_cell_counts else 0,
        'max_cells': max(data_cell_counts) if data_cell_counts else 0,
        'variance': variance,
        'is_consistent': not corrupted_rows,
        'corrupted_rows': corrupted_rows,
        'tolerance': tolerance,
    }

    return is_valid, diagnostics


def filter_markdown_content(content: str, filename: str) -> str:
    """
    Filter markdown content: skip table blocks if file is in EXCLUDE list.

    Args:
        content: Full markdown file content
        filename: Filename or path (used for exclusion matching)

    Returns:
        Filtered content (tables removed if file is excluded)
    """
    if should_process_tables_in_file(filename):
        return content

    # Remove table blocks
    lines = content.split('\n')
    blocks = extract_table_blocks(lines)

    # Mark table blocks for removal
    remove_ranges = set()
    for block in blocks:
        for i in range(block['start_line'], block['end_line'] + 1):
            remove_ranges.add(i)

    # Reconstruct content without table lines
    filtered_lines = [line for i, line in enumerate(lines) if i not in remove_ranges]
    return '\n'.join(filtered_lines)


def add_table_warning(content: str, filename: str) -> str:
    """
    Add validation warnings to markdown if file has high-risk tables.
    """
    if not is_high_risk_file(filename):
        return content

    warning = (
        "\n⚠️ **Data Quality Note:** This document contains wide tables (>10 columns) "
        "from PDF-to-Markdown conversion. Table cell alignment may be compromised. "
        "Critical data has been manually verified against original PDFs.\n\n"
    )

    # Insert at top, after YAML frontmatter if present
    if content.startswith('---'):
        # Find closing frontmatter
        lines = content.split('\n')
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == '---':
                return '\n'.join(lines[:i+1]) + warning + '\n'.join(lines[i+1:])

    return warning + content


if __name__ == '__main__':
    # Quick test
    test_content = """
# Test Table

| Col A | Col B | Col C |
|-------|-------|-------|
| a1    | b1    | c1    |
| a2    | b2    |       |
| a3    | b3    | c3    |
"""

    lines = test_content.strip().split('\n')
    blocks = extract_table_blocks(lines)
    print(f"Found {len(blocks)} table block(s)")

    for block in blocks:
        is_valid, diags = validate_table_block(block['rows'])
        print(f"Block is_valid: {is_valid}")
        print(f"Diagnostics: {diags}")
