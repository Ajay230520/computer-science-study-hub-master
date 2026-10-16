# Digital Image Processing Practicals

## Practical 2 — Image analysis and histograms

[**Open runnable Jupyter notebook**](02-image-analysis-histograms.ipynb)

The notebook reads two grayscale sample images, calculates minimum, maximum, mean, standard deviation and mode, normalizes intensity values to [0,1], and plots separate and combined histograms.

### Free assets and dependencies

The notebook uses `skimage.data.camera()` and `skimage.data.coins()`, sample images bundled with the open-source scikit-image Python package. They load locally after installing the package; no paid API or download is needed during the notebook run.

Install:
`python -m pip install jupyter numpy matplotlib scipy scikit-image`

### Interpretation cautions

- Per-image min-max normalization maps each image's own range to [0,1]; it does not equalize the distributions.
- A combined raw histogram uses pixel counts, so image dimensions affect the count scale. Density-normalized histograms are more suitable when comparing distribution shapes across different image sizes.
- The mode function resolves ties by selecting the smallest most-frequent intensity.
- Verify image asset licensing before extracting and redistributing raw sample images outside the package.
