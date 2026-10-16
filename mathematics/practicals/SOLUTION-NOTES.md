# MFCS Practical Solution Notes

These notes accompany the runnable notebooks. Use the notebook for executable calculations and plots.

## Practical 1 — Classical and empirical probability

- Classical probability for a fair coin: P(H)=1/2.
- Empirical estimate after N trials: number of observed heads / N.
- Expected observation: the cumulative empirical estimate fluctuates, especially early, and often settles closer to 0.5 as the number of independent trials increases. It need not approach monotonically.

## Practical 3 — Geometric distribution

For a first success on trial k with success probability p:

P(X=k)=(1-p)^(k-1)p, for k=1,2,...

Using the provided 30-slot wheel:
- Red: p=18/30=0.6
- Black: p=10/30=1/3
- Green: p=2/30=1/15

Higher p produces greater probability of an early first win. The plotted range 1–20 omits the tail after trial 20.

## Practical 4 — Negative binomial distribution

For the r-th success on trial n:

P(N=n)=C(n-1,r-1)p^r(1-p)^(n-r), n≥r.

Here r=5. The probability is zero for n<5. Higher success probability generally shifts the fifth success toward earlier trials. The supplied wheel probabilities are the same as Practical 3.

## Practical 5 — Binomial and Poisson distributions

Binomial PMF:

P(X=x)=C(n,x)p^x(1-p)^(n-x).

Poisson PMF:

P(X=x)=e^(-λ) λ^x / x!, where λ=np is used for the approximation.

For the supplied n=1000 scenarios:
- Case 1: p=250/2500=0.1 and λ=100. P(X=2) is extraordinarily small.
- Case 2: p=1/2500=0.0004 and λ=0.4. Binomial and Poisson P(X=2) are approximately 0.05361 and 0.05363 respectively.

**Source verification warning:** Case 1's rate (10%) is 250 times the Case 2 rate (0.04%). These are the values written in the supplied PDF. Verify Case 1 with the instructor before presenting it as a real-world prevalence estimate. No medical inference should be drawn from this classroom scenario.

## Practical 6 — Random sampling

Generate a population of 1,000 random integers and calculate its mean, variance, and standard deviation. Draw samples of sizes 10, 50, 100, 200, and 400 and calculate the corresponding statistics.

- Population variance: use ddof=0.
- Sample variance: ddof=1 is the usual unbiased estimator under standard random-sampling assumptions.
- Larger samples often yield more stable estimates, but individual sample estimates do not have to improve monotonically.
- Standard deviation is in the original units; variance is in squared units.

## Reference and software

The scenario wording and requested tasks follow the uploaded course practical sheets. Implementations use NumPy, Matplotlib, SciPy, and pandas where useful. Consult official documentation:
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/
- SciPy statistics: https://docs.scipy.org/doc/scipy/reference/stats.html
- pandas: https://pandas.pydata.org/docs/
- scikit-image sample data: https://scikit-image.org/docs/stable/api/skimage.data.html
