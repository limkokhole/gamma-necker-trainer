# gamma-necker-trainer

A minimal Python demo that pairs a **bold-cued Necker cube** with a **40 Hz auditory click-train** so you can test how γ-band entrainment plus short-term perceptual learning alters the rate (and subjective control) of reversible-depth flips.

## What the script does
- **Teach (0–30 s)** — The left cube alternates bold edges every 3 s; a 0.5-s burst of 40 Hz clicks also repeats every 3 s — **use each burst as a cue to consciously flip the cube’s depth**.

- **Test (30 s onward)** — The left cube auto-minimises; keep listening to the click-beat and **keep flipping the now-ambiguous cube at every burst** to gauge how well the trained rhythm sticks.

- **Optional depth load** — An inner Necker cube is built-in to increase figure–ground binding demands, a manipulation linked to stronger γ activity in V2/V4 models. 
  References: [Physiology Journals](https://journals.physiology.org/doi/full/10.1152/jn.00203.2007), [PMC1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4912377/), [PMC2](https://pmc.ncbi.nlm.nih.gov/articles/PMC1564069/)

![Alt text](/images/screenshot.png?raw=true "First 30 seconds")

## What’s the point?
| **Goal** | **Neuroscience benefit** | **Key references** |
|---|---|---|
| Probe γ-entrainment in a browser-sized experiment | Click-trains every 25 ms elicit a strong 40 Hz auditory steady-state response (ASSR), a canonical marker of network synchrony that scales with cognitive performance. | [PubMed](https://pubmed.ncbi.nlm.nih.gov/31589626/), [NCBI](https://www.ncbi.nlm.nih.gov/books/NBK597346/) |
| Demonstrate cross-modal spread of γ | Although maximal in auditory cortex, ASSR propagates to parietal and frontal hubs, offering a low-cost way to modulate networks that arbitrate bistable perception. | [Nature](https://www.nature.com/articles/s41586-024-07132-6), [PNAS](https://www.pnas.org/doi/10.1073/pnas.1402773111), [Picower Institute](https://picower.mit.edu/news/review-evidence-expanding-40hz-gamma-stimulation-promotes-brain-health) |
| Train depth priors in 30 s | A single half-minute of bold-edge cueing biases later interpretations of the cube for up to an hour, illustrating how short perceptual learning episodes reshape top-down expectations. | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9582357/), [Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1160605/full), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3309967/) |
| Quantify or just experience reversals | Users can simply “feel” the rhythm—or log key-presses to compute alternation rates, a heritable trait tied to parietal anatomy and attentional control. | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5467698/), [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00979/full) |
| Serve as a teaching & pilot-data tool | The script distils core concepts—γ synchrony, figure/ground binding, volitional control—into < 100 lines of code runnable in class or lab meetings. | [PubMed](https://pubmed.ncbi.nlm.nih.gov/21194550/), [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1053811918321359) |
| Bridge to therapeutic research | 40 Hz sensory stimulation (GENUS) is under active trial for Alzheimer’s; this unimodal variant offers a sandbox for mechanism testing without proprietary hardware. | [WIRED](https://www.wired.com/story/cognito-wearable-device-light-sound-treatment-alzheimers-dementia), [Nature](https://www.nature.com/articles/s41586-024-07132-6) |

## Why this matters
- γ bursts precede – or in some labs, accompany – a flip — EEG/MEG show 30-50 Hz power peaks ~200 ms before each Necker-cube reversal, especially over parietal–occipital site ([Taylor & Francis Online](https://www.tandfonline.com/doi/abs/10.1080/13506280143000151), [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0167876005001273)).

- 40 Hz click-trains (the burst acts as a ‘flip-now’ cue) lock phase in auditory cortex and can propagate to fronto-parietal networks (auditory steady-state response, ASSR) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4946051/), [The Journal of Neuroscience](https://www.jneurosci.org/content/44/24/e2029232024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20413346/)).

- Multisensory 40 Hz (GENUS) spreads even further, but this repo is intentionally unimodal so the visual task and the auditory metronome stay separable ([Picower Institute](https://picower.mit.edu/news/review-evidence-expanding-40hz-gamma-stimulation-promotes-brain-health), [MIT News](https://news.mit.edu/2025/evidence-40hz-gamma-stimulation-promotes-brain-health-expanding-0314), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10842797/)).

- Brief disambiguation trains a bias—seeing the cube with forced depth for 20–60 s shifts later interpretation of the ambiguous version for minutes to days ([Journal of Vision](https://jov.arvojournals.org/article.aspx?articleid=2191673), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3118412/), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3217240/)).

- Reversal speed is highly individual and correlates with parietal anatomy and intrinsic network dynamics, so within-subject designs are essential ([PubMed](https://pubmed.ncbi.nlm.nih.gov/20727757/), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1403736/), [Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.00589/full)).

## Neuroscience-relevant uncertainties
| **Issue** | **Evidence-based Note** |
|-----------------------------------------|----------------------------------|
| **Propagation of auditory γ** | ASSR is maximal in auditory cortex; spread to visual/parietal areas is weaker than with audiovisual 40 Hz stimulation. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4946051/), [PubMed](https://pubmed.ncbi.nlm.nih.gov/40034515/) |
| **Attentional load** | High visuospatial or working-memory load can suppress 40 Hz auditory responses. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3711011/), [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S000169181930455X) |
| **Transfer to other figures** | Training effects generalise poorly from cubes to unrelated bistable images; confirm with additional stimuli if needed. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1053811915005583) |
| **Nested-cube effect size** | Empirical data on how multi-layer depth modulates γ is still sparse and sometimes contradictory. [Physiology Journals](https://journals.physiology.org/doi/full/10.1152/jn.00203.2007), [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0042698908004914) |

---

## Disclaimer

This repository is a research and teaching sandbox.  
It is **not** a medical, diagnostic, or therapeutic device and has **not** been evaluated by any regulatory agency.  
All code and documentation are provided “as is,” without warranty of any kind.  
Use at your own risk, and always comply with your local ethics and safety guidelines when running human-subject experiments.

**Author note:** I am not a neuroscientist; all background references were gathered with the help of ChatGPT and verified to the best of my ability.


