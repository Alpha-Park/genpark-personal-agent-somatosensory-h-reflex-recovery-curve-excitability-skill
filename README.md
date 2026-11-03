# Somatosensory H-Reflex Recovery Curve Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Hoffmann Reflex (H-reflex) paired-pulse recovery ratios ($H_2/H_1\%$), Early Depression Index (EDI), and Central Spinal Disinhibition Index across inter-stimulus intervals.

## Architecture

```mermaid
flowchart TD
    A[Tibial Nerve Paired Stimuli S1 & S2] --> B[Record EMG H1 & H2 Amplitudes]
    B --> C[Compute Recovery Ratio H2/H1% Across ISIs]
    C --> D[Calculate Early Depression Index EDI]
    D --> E[Classify Normal Presynaptic Inhibition vs Spastic Disinhibition]
```

## Quickstart

```python
from client import HReflexRecoveryCurveClient

client = HReflexRecoveryCurveClient()
result = client.evaluate_recovery_curve(
    h1_baseline_amplitude_mv=3.5,
    isi_responses=[
        {"isi_ms": 50.0, "h2_amplitude_mv": 0.20},
        {"isi_ms": 100.0, "h2_amplitude_mv": 0.50},
        {"isi_ms": 200.0, "h2_amplitude_mv": 1.40},
        {"isi_ms": 500.0, "h2_amplitude_mv": 3.10}
    ]
)
print(result)
```

## License

Apache-2.0
