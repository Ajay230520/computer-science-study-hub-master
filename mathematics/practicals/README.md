# MFCS Practical Lab

Runnable Jupyter notebooks and concise solution notes for the supplied MFCS practicals.

## Practical index

| Practical | Topic | Runnable notebook |
|---|---|---|
| 1 | Classical and empirical probability | [Open notebook](01-classical-empirical-probability.ipynb) |
| 3 | Geometric distribution | [Open notebook](03-geometric-distribution.ipynb) |
| 4 | Negative binomial distribution | [Open notebook](04-negative-binomial-distribution.ipynb) |
| 5 | Binomial and Poisson distributions | [Open notebook](05-binomial-poisson-distributions.ipynb) |
| 6 | Random sampling | [Open notebook](06-random-sampling.ipynb) |

Practical 2 is image analysis and is stored under [Digital Image Processing practicals](../../digital-image-processing/practicals/README.md).

## Run locally

1. Install Python 3.10 or later.
2. Create and activate a virtual environment if desired.
3. Install dependencies:
   `python -m pip install jupyter numpy matplotlib pandas scipy scikit-image`
4. Start Jupyter: `jupyter lab`
5. Open a notebook and choose **Run → Run All Cells**.

Google Colab can also run the notebooks. For Practical 2, run the notebook's install cell if scikit-image is unavailable.

## Reproducibility and correctness notes

- Notebooks set random seeds where randomness is involved.
- The supplied Practical 5 PDF states two different rates: Case 1 uses 250/2500 = 0.1; Case 2 uses 1/2500 = 0.0004. The notebook preserves those values and flags Case 1 for instructor verification rather than silently changing the source.
- Practical 6 explicitly reports variance conventions: population variance uses ddof=0; sample variance with ddof=1 is also shown.
- Roulette examples are probability exercises only, not gambling advice.
- The source practical PDFs are references supplied for this work; the notebooks contain runnable implementations and interpretations. Confirm formatting/output requirements with the course instructor.

## Learning workflow

Read the aim and formula, run each cell in order, explain the output in your own words, then write observations in your lab record. Do not report a practical as mastered until you can explain the formula and interpret its graph/output without copying the notebook.
