"""
Example usage of Somatosensory H-Reflex Recovery Curve Skill.
Demonstrates normal spinal presynaptic inhibition vs upper motor neuron spastic disinhibition.
"""

import json
from client import HReflexRecoveryCurveClient


def main():
    print("=== Testing H-Reflex Recovery Curve Skill ===")
    client = HReflexRecoveryCurveClient()

    # 1. Healthy young subject (H1 = 3.5 mV, at 50ms H2=0.2mV (5.7%), at 100ms H2=0.5mV (14.3%), at 200ms H2=1.4mV (40%), at 500ms H2=3.1mV (88.6%))
    res_normal = client.evaluate_recovery_curve(
        h1_baseline_amplitude_mv=3.5,
        isi_responses=[
            {"isi_ms": 50.0, "h2_amplitude_mv": 0.20},
            {"isi_ms": 100.0, "h2_amplitude_mv": 0.50},
            {"isi_ms": 200.0, "h2_amplitude_mv": 1.40},
            {"isi_ms": 500.0, "h2_amplitude_mv": 3.10},
            {"isi_ms": 1000.0, "h2_amplitude_mv": 3.45}
        ],
        m_max_amplitude_mv=7.0
    )
    print("\n[Case 1: Normal Spinal Inhibition]")
    print(json.dumps(res_normal, indent=2))

    # 2. Spastic stroke / Upper Motor Neuron lesion (Early depression abolished: at 50ms H2=1.8mV (51.4%), at 100ms H2=2.4mV (68.6%))
    res_spastic = client.evaluate_recovery_curve(
        h1_baseline_amplitude_mv=3.5,
        isi_responses=[
            {"isi_ms": 50.0, "h2_amplitude_mv": 1.80},
            {"isi_ms": 100.0, "h2_amplitude_mv": 2.40},
            {"isi_ms": 200.0, "h2_amplitude_mv": 2.90},
            {"isi_ms": 500.0, "h2_amplitude_mv": 3.40},
            {"isi_ms": 1000.0, "h2_amplitude_mv": 3.50}
        ],
        m_max_amplitude_mv=7.0
    )
    print("\n[Case 2: Pathological Spinal Disinhibition (Spasticity)]")
    print(json.dumps(res_spastic, indent=2))

    # Assertions
    assert res_normal["indices"]["early_depression_index_pct"] < 20.0
    assert "Normal" in res_normal["neurophysiological_assessment"]["excitability_state"]
    assert res_spastic["indices"]["early_depression_index_pct"] > 40.0
    assert "Disinhibition" in res_spastic["neurophysiological_assessment"]["excitability_state"]
    print("\n[SUCCESS] H-Reflex Recovery Curve tests passed!")


if __name__ == "__main__":
    main()
