---
name: genpark-personal-agent-somatosensory-h-reflex-recovery-curve-excitability-skill
version: 1.0.0
description: Calculates Hoffmann Reflex (H-reflex) paired-pulse recovery ratios (H2/H1%), Early Depression Index, and Central Spinal Disinhibition Index across inter-stimulus intervals.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - neurophysiology
  - h-reflex
  - motoneuron
  - spasticity
  - zero-dependency
---

# Somatosensory H-Reflex Recovery Curve Skill

## Mathematical Formulation

Paired-pulse reflex amplitude ratio:

$$R(\text{ISI}) = \left(\frac{H_2(\text{ISI})}{H_1}\right) \times 100 \quad (\%)$$

Early Depression Index (EDI, short $\text{ISI} \le 120\text{ ms}$):

$$\text{EDI} = \frac{1}{N_{\text{early}}} \sum_{i \in \text{early}} R(\text{ISI}_i)$$

Maximal motor ratio:

$$H_{\max}/M_{\max} \, (\%) = \left(\frac{H_1}{M_{\max}}\right) \times 100$$

## Clinical Neurophysiology
- **Physiological Inhibition**: $\text{EDI} \le 20\%$ (strong presynaptic transmitter depletion and Renshaw recurrent inhibition)
- **Borderline Disinhibition**: $\text{EDI} \in [25\%, 40\%]$
- **Pathological Spastic Disinhibition**: $\text{EDI} \ge 40\%$ (loss of descending corticospinal presynaptic inhibition; hallmark of spastic paresis, dystonia, or upper motor neuron syndrome)
