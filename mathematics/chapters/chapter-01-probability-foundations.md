# Chapter 1 — Probability Foundations and Random Variables

> **Course:** Mathematical Foundation of Computer Science (ME01000621)  
> **Level:** Start from zero; no probability background assumed  
> **Purpose:** Understand uncertainty well enough to solve MFCS problems and use probability in machine learning, software systems, computer vision and engineering.  
> **Status:** Learning notes — Chapter 1, Part 1  
> **How to study:** Read one numbered topic, reproduce the worked example on paper, then attempt the linked practice. Do not memorise a formula before understanding what it counts.

---

## Chapter roadmap

| Topic | What you will be able to do | Assignment / practical connection |
|---|---|---|
| 1.1 Why probability? | Describe uncertainty numerically and distinguish probability from a guarantee | Assignment 1 Q1–Q2; Unit 1 Q17 |
| 1.2 Random experiment, outcome and sample space | List all possible results without missing or double-counting | Assignment 2 Q3; Unit 1 Q10 |
| 1.3 Events and event operations | Translate AND, OR, NOT and “at least” into sets | Unit 1 Q6, Q16, Q24 |
| 1.4 Probability rules | Apply the range, total probability, complement and addition rules | Assignment 1 Q3; Unit 1 Q14 |
| 1.5 Conditional probability | Recalculate probability after receiving information | Assignment 1 Q4–Q5; Unit 1 Q22 |
| 1.6 Independence and dependence | Decide whether one event changes another event's probability | Assignment 1 Q4; Unit 1 Q16 |
| 1.7 Counting and combinations | Count possible selections before calculating probability | Assignment 2 Q5; Unit 1 Q11, Q17 |
| 1.8 Random variables and distributions | Convert outcomes into numbers and describe their probabilities | Unit 1 Q4, Q13, Q20, Q21, Q26, Q28 |
| 1.9 PMF and discrete distributions | Build and check a probability mass function | Unit 1 Q4, Q12, Q13, Q20, Q21, Q26, Q28 |
| 1.10 PDF and continuous distributions | Understand density, area and normalization | Assignment 2 Q6–Q8; Unit 1 Q2, Q23, Q27 |
| 1.11 CDF | Calculate probability up to a threshold and between two values | Unit 1 Q2, Q12, Q13, Q23, Q26–Q28 |
| 1.12 Expectation and variance | Calculate long-run average and spread | Assignment 1 Q1–Q2; Assignment 2 Q1; Unit 1 Q3–Q5, Q10, Q19, Q21 |
| 1.13 Conditional expectation | Calculate an average after restricting to known information | Unit 1 Q25 |
| 1.14 CLT and sampling intuition | Understand why sample averages become more stable | Unit 1 Q1, Q15, Q18; Practical 6 |
| 1.15 Probability inequalities | Bound risk when the full distribution is unknown | GTU Unit 1 topic; connect after expectation/variance |
| 1.16 Markov chains | Model systems that move between states over time | GTU Unit 1 topic; software/network applications |

**Syllabus alignment:** The supplied GTU ME01000621 reference lists Unit 1 as probability fundamentals; PMF, PDF and CDF; parametric distributions; expectation, variance and conditional expectation; univariate and multivariate CLT; probabilistic inequalities; and Markov chains (7 hours, 15% in that reference). The supplied syllabus is labelled A.Y. 2024–25; confirm current applicability with LDCE/GTU.

---

## 1.1 Why do we need probability?

### Start with a real situation

Imagine an online shopping company ships 10,000 phones. From previous quality records, around 2% of phones are defective.

Can the company identify exactly which phone will fail before testing it? Usually, no. But it can estimate the risk:

- Number shipped = 10,000
- Defect rate = 2% = 0.02
- Expected defective phones = 10,000 × 0.02 = 200

**Important:** 200 is an average expectation, not a promise that exactly 200 phones will be defective in every shipment.

### Meaning

Probability is a numerical way to describe how likely an event is.

- 0 means impossible under the model.
- 1 means certain under the model.
- 0.5 means a 50% chance.

For an event A:

\[
0 \leq P(A) \leq 1
\]

To convert a probability into a percentage, multiply by 100.

Example: P(A) = 0.25 = 25%.

### Probability is not a guarantee

If a weather forecast says 70% chance of rain, it does not mean it will rain for 70% of the day. It describes uncertainty for the forecast's defined location, period and event.

### Where computer science uses it

1. **Machine learning:** a classifier may estimate P(spam | email features) = 0.92.
2. **Cybersecurity:** estimate the chance that a login attempt is fraudulent.
3. **Reliability engineering:** estimate the chance a server fails during a time interval.
4. **Computer vision:** estimate the probability that an image contains a pedestrian.
5. **Networks:** model packet loss, traffic arrivals and queue delays.

### Quick check

A model predicts a 0.8 probability of a server remaining operational for the next hour. Does that guarantee the server will stay online?

**Answer:** No. It represents an 80% modelled probability, not certainty.

---

## 1.2 Random experiment, outcome and sample space

These three words are the foundation. Keep them separate.

### Random experiment

A process whose exact result is not known before it happens, even though its possible results are known.

Examples:
- Tossing a coin.
- Selecting one component from a production line.
- Recording whether a server request succeeds.
- Measuring how long a user waits for a bus.

### Outcome

One particular result of the experiment.

For one coin toss:
- H = Head
- T = Tail

H is one outcome. T is another outcome.

### Sample space

The set of **all possible outcomes**. It is commonly written as S or Ω.

For one coin toss:

\[
S = \{H,T\}
\]

For one six-sided die:

\[
S = \{1,2,3,4,5,6\}
\]

For two coin tosses, order matters:

\[
S = \{HH, HT, TH, TT\}
\]

There are four outcomes, not three. HT and TH are different because the first and second tosses are different positions.

### Real-life example: API request

Suppose one API request can be:
- S = successful response
- F = failed response

Then S = {S, F}. If 970 of 1,000 requests succeed, the observed success rate is 970/1000 = 0.97.

### A reliable method to list a sample space

1. Define exactly what one experiment means.
2. Decide whether order matters.
3. List every possible result.
4. Check that no result is repeated or missing.
5. Check that outcomes are mutually exclusive for that experiment.

**Common mistake:** For two tosses, writing {HH, HT, TT} and forgetting TH.

---

## 1.3 Events and event operations

An event is a collection (subset) of outcomes from the sample space.

For a die roll:

\[
S=\{1,2,3,4,5,6\}
\]

Let:
- A = getting an even number = {2, 4, 6}
- B = getting a number greater than 3 = {4, 5, 6}

### NOT A: complement

Aᶜ means A does not happen.

\[
A^c = \{1,3,5\}
\]

### A OR B: union

A ∪ B means A happens, or B happens, or both happen.

\[
A \cup B = \{2,4,5,6\}
\]

### A AND B: intersection

A ∩ B means both A and B happen.

\[
A \cap B = \{4,6\}
\]

### Mutually exclusive events

Two events are mutually exclusive if they cannot happen in the same trial.

Example: on one die roll, “get 2” and “get 5” cannot both happen.

\[
A \cap B = \varnothing
\]

Do not confuse mutually exclusive with independent. Mutually exclusive events with non-zero probabilities are not independent.

### Translation table

| Words in a question | Mathematical meaning |
|---|---|
| not A, does not happen | Aᶜ |
| A or B, at least one | A ∪ B |
| A and B, both | A ∩ B |
| neither A nor B | (A ∪ B)ᶜ |
| A only | A ∩ Bᶜ |
| exactly one of A and B | (A ∩ Bᶜ) ∪ (Aᶜ ∩ B) |

### Worked example

A die is rolled once. Find the outcomes for “even OR greater than 3”.

A = {2,4,6}; B = {4,5,6}.

Combine both sets without duplicating common values:

\[
A\cup B=\{2,4,5,6\}
\]

There are 4 favourable outcomes out of 6 equally likely outcomes, so:

\[
P(A\cup B)=\frac{4}{6}=\frac{2}{3}
\]

---

## 1.4 Probability rules

### Rule 1 — Probability range

\[
0\leq P(A)\leq 1
\]

### Rule 2 — Certain event

\[
P(S)=1
\]

Something in the sample space must happen.

### Rule 3 — Impossible event

\[
P(\varnothing)=0
\]

### Rule 4 — Complement rule

\[
P(A^c)=1-P(A)
\]

**Why useful?** “At least one” is often easier to solve by calculating “none” first.

Example: A user has a 10% probability of making an incorrect password attempt on one login. Under an independent-attempt model, the probability of no incorrect attempt in one attempt is 1 − 0.10 = 0.90.

### Rule 5 — Addition rule

For any two events:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]

Why subtract the intersection? Because adding P(A) and P(B) counts the shared outcomes twice.

If A and B are mutually exclusive, the intersection is zero:

\[
P(A\cup B)=P(A)+P(B)
\]

### Worked example: software alerts

In 100 monitoring alerts:
- 30 relate to CPU usage (A)
- 20 relate to memory usage (B)
- 8 relate to both CPU and memory

Then:

\[
P(A\cup B)=0.30+0.20-0.08=0.42
\]

So 42% of alerts concern CPU, memory, or both.

**Check:** The answer cannot be 50%, because the 8 overlapping alerts were counted twice in 30 + 20.

---

## 1.5 Conditional probability

### The central idea

Conditional probability means calculating probability after some information is already known.

The phrase **“given that B happened”** changes the group of outcomes we are considering. We now work only inside B.

Formula:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0
\]

Read it as: probability of A given B.

### Visual intuition

Imagine 100 students:
- 40 know Python.
- 25 know both Python and SQL.

Let A = knows Python, B = knows SQL. If 50 students know SQL, then among those 50 SQL students, 25 know Python:

\[
P(A\mid B)=\frac{25}{50}=0.5
\]

Do not divide by all 100. The condition “given SQL” restricts the denominator to SQL students.

### Worked example: quality inspection

Out of 200 devices:
- 20 are defective.
- 15 are defective and fail the first test.
- 30 fail the first test in total.

Let D = defective and F = fails first test.

\[
P(D\mid F)=\frac{P(D\cap F)}{P(F)}
=\frac{15/200}{30/200}
=\frac{15}{30}=0.5
\]

Among devices that failed the first test, 50% are defective.

### Two-step question pattern

If a question says “given that B”, do this:
1. Identify B.
2. Use only B cases in the denominator.
3. Of those B cases, count cases that also satisfy A.
4. Divide both-and cases by B cases.

**Assignment mapping:** Assignment 1 Q3 asks total probability and Bayes using late flights; Q4 compares conditional with unconditional probabilities; Q5 uses a conditional probability from a fish-consumption table. Unit 1 Q22 is a Bayes/conditional-probability technician problem.

---

## 1.6 Independence and dependence

Two events A and B are independent when knowing that B happened does not change the probability of A.

Equivalent test (when the relevant probabilities are defined):

\[
P(A\mid B)=P(A)
\]

or

\[
P(A\cap B)=P(A)P(B)
\]

### Example: independent coin tosses

For a fair coin:
- P(first toss is H) = 1/2
- P(second toss is H) = 1/2
- P(both are H) = 1/4

Since (1/2)(1/2) = 1/4, these events are independent.

A previous fair toss does not change the next toss.

### Example: dependent draws without replacement

A bag has 4 red and 6 blue balls. Two balls are drawn without replacement.

Before the first draw:

\[
P(\text{red first})=\frac{4}{10}
\]

If the first ball is red, 3 red remain among 9 balls:

\[
P(\text{red second}\mid\text{red first})=\frac{3}{9}
\]

The probability changed from 4/10 to 3/9, so the draws are dependent.

If the first ball is replaced before the second draw, the original composition returns and the draws are independent (assuming a properly mixed bag).

### Important distinction

- **Mutually exclusive:** cannot happen together.
- **Independent:** one event does not change the probability of the other.

If A and B are mutually exclusive and both have positive probability, they are dependent.

**Assignment mapping:** Assignment 1 Q4 explicitly asks whether a conditional probability is equal to, greater than or less than an unconditional probability. Unit 1 Q16 uses independent pollutant events. Assignment 2 Q3 uses repeated draws with replacement.

---

## 1.7 Counting: permutations and combinations

Before calculating probability, we often need to count how many possible cases exist.

### Multiplication principle

If one task has m choices and a second independent choice has n options, the combined number of ordered possibilities is m × n.

Example: 3 shirt choices and 2 trouser choices give 3 × 2 = 6 outfits.

### Factorial

\[
n!=n(n-1)(n-2)\cdots 2\cdot1,\qquad 0!=1
\]

Example: 4! = 4 × 3 × 2 × 1 = 24.

### Permutation — order matters

Number of ways to arrange r objects selected from n distinct objects:

\[
{}^nP_r=\frac{n!}{(n-r)!}
\]

Example: choosing a president and secretary from 5 people: 5 × 4 = 20. The roles are different, so A-as-president/B-as-secretary is different from B-as-president/A-as-secretary.

### Combination — order does not matter

Number of ways to select r objects from n distinct objects:

\[
{}^nC_r=\frac{n!}{r!(n-r)!}
\]

Example: selecting 2 students from 5 for a team:

\[
{}^5C_2=\frac{5!}{2!3!}=10
\]

The pair {A,B} is the same team as {B,A}.

### Decision rule

Ask: “Would swapping the selected items create a different result?”
- Yes → permutation / ordered counting.
- No → combination / unordered selection.

**Assignment mapping:** Unit 1 Q11 asks about partitioning people into committees; Unit 1 Q17 involves choosing 6 lottery numbers from 49; Assignment 2 Q5 uses a hypergeometric selection problem. These require careful counting, but their full solution methods will be taught in the relevant lessons.

---

## 1.8 Random variables

A random variable is a rule that assigns a numerical value to each outcome of a random experiment.

The variable is usually written as X.

### Example: two coin tosses

Sample space:

\[
S=\{HH,HT,TH,TT\}
\]

Let X = number of heads.

| Outcome | Value of X |
|---|---:|
| HH | 2 |
| HT | 1 |
| TH | 1 |
| TT | 0 |

X is a random variable because its value depends on the random result.

### Discrete random variable

A variable that takes countable values, such as:
- Number of defective components.
- Number of customers arriving in one minute.
- Number of heads in 5 tosses.
- Number of failed requests.

### Continuous random variable

A variable that can take any value in an interval, such as:
- Server response time.
- A person's waiting time.
- Component length.
- Temperature.

A measurement such as 2.1 seconds, 2.13 seconds or 2.137 seconds is possible, depending on measurement precision.

### Why this matters

A probability distribution describes how probability is assigned to the values of X. It lets us move from a story (“requests sometimes fail”) to a mathematical model we can calculate, simulate and test.

---

## 1.9 PMF — Probability Mass Function

A PMF is used for a **discrete** random variable. It gives the probability of each exact value.

\[
p_X(x)=P(X=x)
\]

A valid PMF must satisfy:
1. Every probability is between 0 and 1.
2. The probabilities of all possible values add to 1.

\[
\sum_x p_X(x)=1
\]

### Worked example: number of heads in two fair tosses

There are four equally likely outcomes: HH, HT, TH, TT.

Let X = number of heads.

| x | Outcomes | P(X = x) |
|---:|---|---:|
| 0 | TT | 1/4 |
| 1 | HT, TH | 2/4 = 1/2 |
| 2 | HH | 1/4 |

Check:

\[
\frac14+\frac12+\frac14=1
\]

So this is a valid PMF.

### Real-life example: failed API calls

Suppose X is the number of failed calls in a fixed batch of 5 requests. X can be 0, 1, 2, 3, 4 or 5. A PMF can tell the engineering team the probability of each failure count.

**Assignment mapping:** Unit 1 Q4 asks to find an unknown constant k, mean and variance from a discrete probability table. Q13 asks for the definition of a probability distribution and PMF. Q20, Q21, Q26 and Q28 also use discrete distributions.

---

## 1.10 PDF — Probability Density Function

A PDF is used for a **continuous** random variable. It describes probability density, not the probability at one exact point.

For a continuous X with density f(x):

\[
f(x)\geq0
\]

and the total area under the PDF over its full support must be 1:

\[
\int_{-\infty}^{\infty}f(x)\,dx=1
\]

Probability between a and b is the area under the curve:

\[
P(a\leq X\leq b)=\int_a^b f(x)\,dx
\]

For a continuous variable:

\[
P(X=a)=0
\]

This does **not** mean the value a is impossible. It means one exact point has zero width and therefore zero area. Intervals can still have positive probability.

### Example: uniform waiting time

A bus arrives every 15 minutes. If your arrival time is equally likely anywhere within one 15-minute interval, your waiting time X can be modelled as uniform from 0 to 15 minutes.

The PDF is:

\[
f(x)=\frac{1}{15},\quad 0\leq x\leq15
\]

The total area is rectangle width × height:

\[
15\times\frac{1}{15}=1
\]

Probability that the wait is less than 5 minutes:

\[
P(X<5)=\int_0^5\frac{1}{15}\,dx
=\frac{5}{15}=\frac13
\]

**Intuition:** probability is area, not the height of the curve.

### Normalization constant

If a PDF contains an unknown constant C, use the total-area rule:

\[
\int_{\text{support}} C\,g(x)\,dx=1
\]

1. Write the correct support (where the density is non-zero).
2. Integrate g(x) over that support.
3. Solve the equation for C.
4. Check that C is positive and the total area is 1.

**Assignment mapping:** Assignment 2 Q6 asks for a normalizing constant and a tail probability; Q7 asks for probabilities over operating-time intervals; Q8 is a uniform waiting-time problem. Unit 1 Q2 and Q23 ask for a normalizing constant and CDF/probability from a PDF.

---

## 1.11 CDF — Cumulative Distribution Function

The CDF tells us the probability that a random variable is less than or equal to a chosen value x.

\[
F_X(x)=P(X\leq x)
\]

### For a discrete variable

Add the PMF probabilities up to x.

Using the two-coin example:

| x | PMF P(X=x) | CDF F(x)=P(X≤x) |
|---:|---:|---:|
| 0 | 1/4 | 1/4 |
| 1 | 1/2 | 3/4 |
| 2 | 1/4 | 1 |

### For a continuous variable

Integrate the PDF from the lower end of its support up to x:

\[
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
\]

For the uniform waiting-time example:

\[
F_X(x)=
\begin{cases}
0,&x<0\\
x/15,&0\leq x\leq15\\
1,&x>15
\end{cases}
\]

Then:

\[
P(5<X\leq10)=F(10)-F(5)
=\frac{10}{15}-\frac{5}{15}
=\frac13
\]

### How PDF and CDF differ

| PDF | CDF |
|---|---|
| Density / curve height | Accumulated probability |
| Area over an interval gives probability | Difference F(b) − F(a) gives interval probability |
| Continuous PDF integrates to 1 | CDF increases from 0 to 1 |
| A PDF height can be greater than 1 | CDF always stays between 0 and 1 |

**Assignment mapping:** Unit 1 Q2 asks for a CDF from a PDF; Q12 asks for a CDF from a discrete count model; Q13 asks for PMF and CDF definitions; Q23, Q26 and Q28 ask for CDF construction.

---

## 1.12 Expectation and variance — first intuition

### Expected value

Expected value is the probability-weighted long-run average of a random variable.

For a discrete X:

\[
E[X]=\sum_x xP(X=x)
\]

### Example: a simple reward

A game gives:
- ₹100 with probability 0.2
- ₹0 with probability 0.8

\[
E[X]=100(0.2)+0(0.8)=₹20
\]

This means the average reward over many plays approaches ₹20 per play under the model. It does not mean every play pays ₹20.

### Variance

Variance measures how spread out values are around the mean.

\[
Var(X)=E[(X-\mu)^2]
=E[X^2]-(E[X])^2
\]

Standard deviation is the square root of variance:

\[
\sigma=\sqrt{Var(X)}
\]

Variance is in squared units; standard deviation is in the original units.

### Practical use

Two servers can have the same average response time but very different variability. A server with highly variable response time may create a worse user experience even if its average looks acceptable.

**Assignment mapping:** Assignment 1 Q1–Q2 and Assignment 2 Q1 involve expected profit/fairness decisions. Unit 1 Q3, Q4, Q5, Q10, Q19 and Q21 involve expected values and/or spread. Full worked methods will be added in the expectation lesson.

---

## 1.13 Conditional expectation — intuition

Conditional expectation is an average calculated after restricting attention to a condition.

\[
E[X\mid A]
\]

means the expected value of X given that event A is known to have happened.

Example: a delivery company calculates the average delivery time for **rainy days only**. This is not the same as the average delivery time across all days.

For a discrete X:

\[
E[X\mid A]=\sum_x xP(X=x\mid A)
\]

**Assignment mapping:** Unit 1 Q25 asks for E(Y | X=1) from a joint probability table. Learn joint distributions before attempting it.

---

## 1.14 Central Limit Theorem — preview

The Central Limit Theorem (CLT) explains why averages of sufficiently large random samples often have an approximately normal distribution, under suitable assumptions.

If X₁, X₂, …, Xₙ are independent and identically distributed with finite mean μ and finite variance σ², then for sufficiently large n the sample mean is approximately:

\[
\bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right)
\]

Standard error:

\[
SE(\bar X)=\frac{\sigma}{\sqrt n}
\]

### Real-life example: website response time

One request can be unusually slow. But if we repeatedly take samples of 100 requests and calculate each sample's average response time, those averages tend to be more stable and often approximately normal when CLT conditions are reasonable.

**Important:** CLT does not say the original data must be normally distributed. It concerns the sampling distribution of the mean. The sample size needed depends on the original distribution and dependence/outliers.

**Assignment mapping:** Unit 1 Q1 asks about CLT applications; Q15 concerns a sample mean over 49 hours; Q18 concerns a sample proportion. Practical 6 compares statistics from different sample sizes.

---

## 1.15 Probabilistic inequalities — preview

Inequalities give bounds on probabilities even when the exact distribution is unknown.

### Markov's inequality

For a non-negative random variable X and a > 0:

\[
P(X\geq a)\leq\frac{E[X]}{a}
\]

It gives an upper bound, not necessarily the exact probability.

Example: if the average number of daily incidents is 2, Markov's inequality says:

\[
P(X\geq10)\leq\frac{2}{10}=0.2
\]

So the probability of 10 or more incidents is at most 20%, given the model assumptions. The actual probability may be much smaller.

Chebyshev's inequality will be studied after variance:

\[
P(|X-\mu|\geq k\sigma)\leq\frac{1}{k^2}
\]

---

## 1.16 Markov chains — preview

A Markov chain models a process that moves between states, where the next-state probabilities depend on the current state (the Markov property).

### Example: website user session

Possible states:
- V = viewing a page
- C = clicking a link
- E = exiting

A transition matrix might describe probabilities such as P(next=C | current=V). Each row must sum to 1.

Markov chains are used in:
- web navigation and ranking,
- queueing and reliability models,
- communication networks,
- user behaviour modelling,
- simple state-based system analysis.

We will study transition matrices and multi-step probabilities after the probability and random-variable basics are secure.

---

## Common mistakes checklist

- Treating expected value as a guaranteed result.
- Forgetting to define the sample space before counting.
- Counting HT and TH as the same outcome when order matters.
- Using the full population as denominator after the words “given that”.
- Confusing independent events with mutually exclusive events.
- Adding P(A) + P(B) without subtracting overlap.
- Using a PMF for a continuous variable or a PDF for a discrete variable.
- Treating PDF height as probability.
- Forgetting that total PMF probability is 1 and total PDF area is 1.
- Thinking P(X = a) must be positive for every possible continuous value.
- Confusing variance units with standard-deviation units.
- Assuming CLT says the raw data become normal.

## Practical coding bridge (Python)

Use the existing free notebooks in [MFCS practicals](../practicals/README.md). They require Python/Jupyter and open-source libraries only.

Suggested first experiment:

1. Simulate 10, 100, 1,000 and 10,000 fair coin tosses.
2. Calculate observed head proportion for each run.
3. Plot the proportion against the number of tosses.
4. Explain why the proportion often gets closer to 0.5 as the number of trials grows, while not necessarily moving closer after every single toss.

Related repository practicals:
- Practical 1 — classical vs empirical probability.
- Practical 3 — geometric distribution.
- Practical 4 — negative-binomial distribution.
- Practical 5 — binomial and Poisson distributions.
- Practical 6 — random sampling.

## Self-test (fresh questions; not copied from assignments)

1. A fair die is rolled. Write the sample space and the event “number is greater than 4”.
2. If P(A)=0.35, find P(not A).
3. In a group of 100 students, 40 know Python, 30 know SQL and 15 know both. Find the probability a randomly selected student knows Python or SQL.
4. Explain in your own words why the denominator changes in P(A | B).
5. A box contains 3 green and 7 yellow balls. One ball is drawn, replaced, and another is drawn. Are the two draws independent? Explain.
6. A fair coin is tossed twice. Define X as the number of tails and write its PMF.
7. A continuous variable has uniform density from 0 to 20. What is the probability it lies between 5 and 9? Explain using area.
8. Explain the difference between PDF and CDF without using only their formulas.

**Learning checkpoint:** Do not mark this chapter reviewed until you can explain the sample space, event operations, conditional probability, independence, PMF/PDF/CDF and expectation in your own words and solve the self-test without copying.

---

## Assignment reference index (prompts only)

This chapter points to the original prompts; it does **not** publish their final answers.

- [Assignment 1](../assignments/assignment-1.md): Q1 expected profit; Q2 expected project value; Q3 total probability and Bayes; Q4 conditional vs unconditional probability; Q5 conditional probability from a data table.
- [Assignment 2](../assignments/assignment-2.md): Q1 expected value/fair game; Q3 repeated draws with replacement; Q5 hypergeometric selection; Q6–Q8 continuous random variables and uniform waiting time.
- [Unit 1 question bank](../assignments/unit-1-question-bank.md): Q1 CLT; Q2 PDF/CDF; Q3 expected defective count and standard deviation; Q4 discrete PMF/mean/variance; Q5–Q6 binomial applications; Q10 expected earnings; Q11 counting; Q12 discrete CDF; Q13 PMF/PDF/CDF definitions; Q14 Poisson; Q15 sample mean; Q16 independent events; Q17 lottery expectation; Q18 sample proportion; Q20–Q28 discrete/continuous distributions, Bayes and conditional expectation.
- [Practical register](../../docs/practicals.html): Practical 1–6, with runnable notebooks and solution notes.

## References for further learning

- Mitzenmacher, M. and Upfal, E., *Probability and Computing* — probability methods used in computer science.
- Trivedi, K. S., *Probability and Statistics with Reliability, Queuing, and Computer Science Applications* — reliability and systems applications.
- SciPy Statistics documentation: https://docs.scipy.org/doc/scipy/reference/stats.html
- NumPy random sampling documentation: https://numpy.org/doc/stable/reference/random/index.html

> **Source integrity:** Assignment prompts are transcribed from repository reference notes. Some original PDF equations/tables were not machine-readable; this chapter flags those cases rather than inventing missing values. Verify the original PDF/instructor version before using incomplete prompts.
