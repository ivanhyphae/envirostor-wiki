---
concept: sampling-frequency
entity_type: technique
aliases: []
sources: ["raw/FW_ SR 132 Basin 5 Clean Fill Sampling Plan .pdf"]
confidence: high
created_at: 2026-06-10T05:02:18Z
---

## Definition

In signal processing and data acquisition, **sampling frequency** (also called sampling rate) is the number of samples taken per unit time (usually in hertz, Hz) from a continuous signal to produce a discrete‑time signal. It determines the temporal resolution of the sampled data and the highest frequency that can be faithfully captured.

## How it works

A continuous signal `x(t)` is converted to a discrete sequence `x[n] = x(n·Ts)`, where `Ts = 1/fs` is the sampling period and `fs` is the sampling frequency. The **Nyquist–Shannon sampling theorem** states that to reconstruct a continuous signal without aliasing, the sampling frequency must be at least twice the highest frequency component present in the signal — this threshold is called the **Nyquist rate**. For example, audio sampled at 44.1 kHz can represent frequencies up to 22.05 kHz.

In practice, an analog anti‑aliasing filter is applied before sampling to remove frequency components above half the sampling frequency (the Nyquist frequency). The discrete samples are then quantized (assigned a digital value) by an analog‑to‑digital converter (ADC). The choice of `fs` directly influences the maximum observable bandwidth of the acquired signal.

## Variants

- **Uniform sampling** – samples are taken at constant intervals (`Ts` constant). The most common method, used in most digital audio, video, and telemetry systems.
- **Non‑uniform (asynchronous) sampling** – time between samples varies, often used in event‑driven or level‑crossing systems to reduce data volume when signals are quiescent.
- **Oversampling** – using a sampling frequency significantly higher than the Nyquist rate. Improves signal‑to‑noise ratio and relaxes anti‑aliasing filter requirements, common in high‑resolution audio ADCs.
- **Undersampling (bandpass sampling)** – sampling at a frequency lower than the Nyquist rate of a high‑frequency bandpass signal, relying on a known spectral location to reconstruct the signal without aliasing, used in some radar and communication receivers.
- **Multirate sampling** – different parts of a system operate at different sampling frequencies, linked by decimation or interpolation (e.g., in software‑defined radios).
- **Adaptive sampling** – the sampling frequency changes based on signal activity to balance accuracy and efficiency.

## Trade-offs

| Consideration          | High sampling frequency                 | Low sampling frequency                     |
|------------------------|------------------------------------------|-------------------------------------------|
| **Fidelity**           | Captures fast‑changing details, less aliasing risk | Loss of high‑frequency content, possible aliasing |
| **Data volume**        | Larger datasets, more storage and bandwidth needed | Smaller datasets, easier to store and transmit |
| **System cost**        | Higher ADC cost, more processing power required | Lower hardware cost, simpler processing   |
| **Power consumption**  | Increases (especially in wireless sensors) | Reduces, extending battery life           |
| **Latency**            | More samples to process may increase delay | Faster processing of fewer samples        |

A key limitation is the **conversion time** of the ADC – the fastest sampling frequency is bounded by the ADC’s conversion rate. Additionally, environmental constraints (e.g., in soil or groundwater monitoring) may dictate a practical limit on how many samples can be physically collected and analyzed.

## See also

- Nyquist–Shannon sampling theorem
- Aliasing
- Anti-aliasing filter
- Quantization (signal processing)
- Digital signal processing
- Analog-to-digital converter
- Oversampling
- Sampling (statistics) (in survey and environmental contexts)