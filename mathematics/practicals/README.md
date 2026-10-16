# MFCS Practical Register

Canonical index for the six practical sheets supplied. Numbers follow the original filenames Practical-1.pdf through Practical-6.pdf. The extra MFCS_Practical5 (1).pdf is an expanded reference for Practical 5, not a seventh practical.

| No. | Original reference file | Practical question / required work | Solution notes | Runnable notebook |
|---:|---|---|---|---|
| 1 | Practical-1.pdf | Implement classical and empirical probability, plot both, discuss larger trial counts, and write observations. | [Solution notes](SOLUTION-NOTES.md#practical-1--classical-and-empirical-probability) | [Run Practical 1](01-classical-empirical-probability.ipynb) |
| 2 | Practical-2.pdf | Read and analyse two images; normalize values; calculate min, max, mean, standard deviation and mode; create individual and combined histograms. | [Image analysis guide](../../digital-image-processing/practicals/README.md) | [Run Practical 2](02-image-analysis-histograms.ipynb) |
| 3 | Practical-3.pdf | Plot geometric PMFs for the first red, black and green win, n=1–20; discuss differences. | [Solution notes](SOLUTION-NOTES.md#practical-3--geometric-distribution) | [Run Practical 3](03-geometric-distribution.ipynb) |
| 4 | Practical-4.pdf | Plot negative-binomial PMFs for the fifth red, black and green win, n=1–20; discuss differences. | [Solution notes](SOLUTION-NOTES.md#practical-4--negative-binomial-distribution) | [Run Practical 4](04-negative-binomial-distribution.ipynb) |
| 5 | Practical-5.pdf; MFCS_Practical5 (1).pdf | Generate binomial and Poisson distributions for both supplied rates; calculate P(X=2) for n=1000. | [Solution notes](SOLUTION-NOTES.md#practical-5--binomial-and-poisson-distributions) | [Run Practical 5](05-binomial-poisson-distributions.ipynb) |
| 6 | Practical-6.pdf | Generate 1,000 random integers; calculate population statistics; compare samples of size 10, 50, 100, 200 and 400. | [Solution notes](SOLUTION-NOTES.md#practical-6--random-sampling) | [Run Practical 6](06-random-sampling.ipynb) |

## Run locally
Install Python 3.10+ then run:
```bash
python -m pip install jupyter numpy matplotlib pandas scipy scikit-image
jupyter lab
```
Open a notebook and choose Run → Run All Cells. No paid dataset or API is required.

## Source and data notes
- The second Practical 5 PDF is treated as an expanded reference, not a seventh practical.
- Practical 5 Case 1 is preserved as written: 250/2500 = 0.1. Case 2 is 1/2500 = 0.0004. Verify Case 1 with the instructor before presenting it as a real-world rate.
- Roulette practicals are probability exercises, not gambling advice.
- Original PDFs remain authoritative for submission wording.
- Website source is in docs/ and can be published through GitHub Pages after configuring Pages to use GitHub Actions.
