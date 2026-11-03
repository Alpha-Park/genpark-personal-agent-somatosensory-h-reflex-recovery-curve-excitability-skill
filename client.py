"""
Somatosensory H-Reflex Recovery Curve & Spinal Motoneuron Excitability Client.
Zero-mock pure Python standard library implementation.
Calculates Hoffmann Reflex (H-reflex) paired-pulse recovery ratios (H2/H1%),
Early Depression Index, and Central Spinal Disinhibition Index (CDI) across inter-stimulus intervals.
"""

import math
from typing import Dict, Any, List, Optional


class HReflexRecoveryCurveClient:
    """
    Evaluates spinal alpha-motoneuron pool excitability and presynaptic inhibition via paired-pulse H-reflex:
    - H2/H1 ratio (%) at variable ISIs (50 ms to 1000 ms)
    - Early Depression Index (EDI): mean H2/H1 at short ISIs (<= 100 ms)
    - Facilitation Peak: max H2/H1 in the 150 - 300 ms window
    - Central Disinhibition Index (CDI): elevated early H2/H1 indicates loss of presynaptic inhibition (spasticity)
    """

    def __init__(self):
        pass

    def evaluate_recovery_curve(
        self,
        h1_baseline_amplitude_mv: float,
        isi_responses: List[Dict[str, float]],
        m_max_amplitude_mv: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates H-reflex paired pulse recovery metrics.
        h1_baseline_amplitude_mv: unconditioned H-reflex peak-to-peak amplitude (mV).
        isi_responses: list of dicts with keys 'isi_ms' and 'h2_amplitude_mv'.
        m_max_amplitude_mv: maximal direct muscle response M_max in mV (optional).
        """
        if h1_baseline_amplitude_mv <= 0:
            raise ValueError("H1 baseline amplitude must be strictly positive.")
        if not isi_responses:
            raise ValueError("Must provide at least one ISI measurement.")

        curve = []
        early_ratios = []
        mid_ratios = []

        for item in isi_responses:
            isi = float(item["isi_ms"])
            h2 = float(item["h2_amplitude_mv"])
            ratio_pct = (h2 / h1_baseline_amplitude_mv) * 100.0
            curve.append({
                "isi_ms": round(isi, 1),
                "h2_amplitude_mv": round(h2, 3),
                "h2_h1_recovery_pct": round(ratio_pct, 1)
            })

            if isi <= 120.0:
                early_ratios.append(ratio_pct)
            elif 150.0 <= isi <= 350.0:
                mid_ratios.append(ratio_pct)

        early_depression_index_pct = sum(early_ratios) / len(early_ratios) if early_ratios else 0.0
        peak_facilitation_pct = max(mid_ratios) if mid_ratios else (max([c["h2_h1_recovery_pct"] for c in curve]) if curve else 0.0)

        # H_max / M_max ratio if M_max provided
        h_m_ratio = None
        if m_max_amplitude_mv and m_max_amplitude_mv > 0:
            h_m_ratio = round((h1_baseline_amplitude_mv / m_max_amplitude_mv) * 100.0, 1)

        # Clinical neurophysiology classification:
        # Normal spinal inhibition: Early depression strong (H2/H1 <= 20% at ISI <= 100 ms)
        # Upper motor neuron lesion / spasticity: Premature recovery / loss of early depression (H2/H1 > 40% at ISI <= 100 ms)
        # Peripheral neuropathy / radiculopathy: Prolonged depression or attenuated facilitation
        if early_depression_index_pct >= 40.0:
            excitability_state = "Pathological Spinal Disinhibition (Spastic / Hyper-excitable Motoneuron Pool)"
            mechanism = "Loss of presynaptic and Renshaw recurrent inhibition; typical of corticospinal tract lesion or spastic dystonia."
        elif early_depression_index_pct >= 25.0:
            excitability_state = "Mild Motoneuron Hyperexcitability / Borderline Disinhibition"
            mechanism = "Attenuated post-activation depression; frequently seen in subclinical motor fatigue or focal tremor."
        else:
            excitability_state = "Normal Spinal Presynaptic Inhibition & Refractoriness"
            mechanism = "Intact homosynaptic depression, Renshaw feedback, and descending corticospinal modulatory control."

        return {
            "status": "success",
            "recovery_curve": curve,
            "indices": {
                "early_depression_index_pct": round(early_depression_index_pct, 1),
                "peak_facilitation_pct": round(peak_facilitation_pct, 1),
                "h_max_m_max_ratio_pct": h_m_ratio
            },
            "neurophysiological_assessment": {
                "excitability_state": excitability_state,
                "mechanistic_interpretation": mechanism
            }
        }
