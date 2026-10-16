# MFCS Practical Solutions — Formula, Method and Observations

## Practical 1 — Classical and empirical probability
For a fair coin, classical P(H)=1/2. Empirical probability is observed heads divided by trial count. The notebook simulates 10,000 flips with a fixed seed. The empirical estimate fluctuates more at small sample sizes and often settles nearer 0.5 as trials increase, but need not move monotonically.

## Practical 2 — Image analysis and histograms
The notebook loads two sample images from scikit-image, computes minimum, maximum, mean, standard deviation and mode, normalizes values to [0,1], and plots separate and combined histograms. Min-max normalization is x'=(x−min)/(max−min). Histograms show intensity distributions, not spatial layout; raw counts can be affected by image size.

## Practical 3 — Geometric distribution
For the first success on trial k: P(X=k)=(1−p)^(k−1)p, k=1,2,...
From the 30-slot wheel: red p=18/30=0.6; black p=10/30=1/3; green p=2/30=1/15. Higher p gives greater probability of an early first win. The graph covers n=1..20 only.

## Practical 4 — Negative binomial distribution
For the fifth success on trial n: P(N=n)=C(n−1,4)p^5(1−p)^(n−5), n≥5. Probability is zero for n<5. Higher success probability generally shifts the fifth success to earlier trials. The model assumes independent spins and fixed probabilities.

## Practical 5 — Binomial and Poisson distributions
Binomial: P(X=x)=C(n,x)p^x(1−p)^(n−x). Poisson: P(X=x)=e^(−λ)λ^x/x!, with λ=np.
For n=1000, Case 1 p=250/2500=0.1, λ=100; exactly two events is extraordinarily unlikely. Case 2 p=1/2500=0.0004, λ=0.4; P(X=2) is approximately 0.05361 (binomial) and 0.05363 (Poisson).
**Source caution:** The stated rates differ by a factor of 250. The notebook preserves the PDF values and flags Case 1 for instructor verification. This is not medical guidance.

## Practical 6 — Random sampling
Generate a population of 1,000 integers and compare sample sizes 10, 50, 100, 200 and 400. Population variance uses ddof=0; sample variance with ddof=1 is also shown. Larger samples often yield more stable estimates, but an individual sample estimate need not improve monotonically. Variance has squared units; standard deviation uses original units.

## Official software references
- NumPy: https://numpy.org/doc/
- Matplotlib: https://matplotlib.org/stable/
- SciPy statistics: https://docs.scipy.org/doc/scipy/reference/stats.html
- pandas: https://pandas.pydata.org/docs/
- scikit-image sample data: https://scikit-image.org/docs/stable/api/skimage.data.html
