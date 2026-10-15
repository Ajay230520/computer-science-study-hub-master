---
title: Probability Foundations
subject: Mathematics for Computer Science and ML
status: in-progress
prerequisites: [fractions, ratios, percentages, basic algebra]
learning_objectives:
  - Explain probability intuitively and formally
  - Identify outcomes, sample spaces, and events
  - Calculate elementary probabilities and state assumptions
last_reviewed: 2026-10-15
---

# 1. Probability Foundations

## 1.1 Intuition

Probability is a numerical way to express uncertainty about an event.

Before tossing a fair coin, we do not know whether it will land heads or tails. Under a fair-coin model, each result has probability (1/2). This does not guarantee alternating outcomes or equal counts in every small batch. It describes the chance for one toss under the stated model.

**Where it appears:** weather forecasts, manufacturing quality checks, reliability engineering, medical testing, fraud detection, and ML classification.

Always ask: *What event? Under which assumptions? For what population or time period?*

## 1.2 Formal definition

For a finite sample space (S) whose outcomes are all equally likely, the classical probability of event (A) is

[
P(A)=\frac{|A|}{|S|}
]

- (S): all possible outcomes in the model.
- (A): the event of interest, a subset of (S).
- (|S|): number of outcomes in (S).
- (|A|): number of outcomes satisfying the event.

The counting formula requires equally likely outcomes. For unequal probabilities, add the probabilities of the outcomes in the event. For continuous variables, probability commonly involves integrating a density.

Core rules:

1. (0 \le P(A) \le 1).
2. (P(S)=1).
3. (P(\varnothing)=0).
4. If events (A) and (B) cannot occur together, (P(A\cup B)=P(A)+P(B)).

A probability of 0.25 is 25%. Probability 0 and 1 mean impossible and certain *under the model*.

## 1.3 Vocabulary

| Term | Meaning | Fair-die example |
|---|---|---|
| Experiment | Process with an uncertain result | Roll a die |
| Outcome | One possible result | 4 |
| Sample space | All modeled outcomes | (S=\{1,2,3,4,5,6\}) |
| Event | Set of outcomes | Even number (A=\{2,4,6\}) |
| Complement | Event A does not occur | (A^c=\{1,3,5\}) |
| Probability model | Rules assigning probabilities | Each face has probability (1/6) if the die is fair |

## 1.4 Worked example A — easy: fair coin

**Question:** Probability of heads in one fair toss?

1. Sample space: (S=\{H,T\}); two outcomes.
2. Event: (A=\{H\}); one favorable outcome.
3. Assumption: the coin is fair, so the two outcomes are equally likely.
4. Calculation:

[
P(A)=\frac{|A|}{|S|}=\frac{1}{2}=0.5=50\%
]

**Answer:** 50% under the fair-coin assumption.

**Common error:** Thinking a tails result is “due” after several heads. Independent fair tosses do not work that way.

## 1.5 Worked example B — intermediate: fair die

**Question:** Probability of a number greater than 4?

1. Sample space: (S=\{1,2,3,4,5,6\}).
2. Event: (A=\{5,6\}).
3. Favorable outcomes = 2; total equally likely outcomes = 6.
4. (P(A)=2/6=1/3\approx0.3333=33.33\%\).

**Answer:** (1/3), assuming a fair die.

## 1.6 Worked example C — quality-control sampling

A batch has 100 sensors: 8 defective, 92 non-defective. One item is chosen uniformly at random.

1. Event (D): selected sensor is defective.
2. There are 100 possible selected items.
3. Eight items satisfy event (D).
4. (P(D)=8/100=0.08=8\%\).

**Interpretation:** The chance of choosing a defective item from this specific batch is 8% under uniform selection.

**Limitation:** This alone does not prove future batches also have an 8% defect rate. That requires a justified model of process stability.

## 1.7 Worked example D — an ML dataset

A labelled image dataset contains 1,000 images: 120 show cracked road surfaces and 880 do not. A row is selected uniformly at random.

[
P(\text{crack})=120/1000=0.12=12\%
]

This is the observed class proportion in this dataset, not necessarily the true rate in another city, season, camera system, or sampling process.

A classifier that always predicts “no crack” gets 88% accuracy on this dataset yet detects no cracked roads. For safety-related use, consider recall, precision, class-specific errors, and the cost of missing a crack. This is an illustrative calculation, not a claim about a particular deployed system.

## 1.8 Complement rule

The complement (A^c) means event (A) does not occur. Since either (A) or its complement must happen,

[
P(A)+P(A^c)=1
]

therefore

[
P(A^c)=1-P(A)
]

**Example:** If a package has a 7% chance of arriving late, its chance of not arriving late is (1-0.07=0.93=93\%\), within the same model. “Not late” does not also imply “undamaged”; that is a different event.

## 1.9 Python demonstration

Run the [probability basics example](../code/probability_basics.py). Exact counting and simulation are different: finite simulations estimate probabilities and vary from run to run.

## 1.10 Common misconceptions

- Probability is not a guarantee.
- Outcomes are not automatically equally likely.
- A 90% chance does not guarantee an event happens exactly 9 times in every 10 trials.
- A dataset's class percentage is not automatically the deployment rate.
- High accuracy alone does not guarantee a useful classifier.

## 1.11 Practice — attempt before checking

1. Roll a fair die. Probability of 2?
2. Roll a fair die. Probability of an odd number?
3. A bag contains 3 red and 7 blue tokens. Select one uniformly. Probability it is red?
4. A dataset has 45 positive and 155 negative examples. What is the positive-class proportion? Why might deployment differ?
5. If (P(A)=0.37), calculate (P(A^c)).
6. A model has 98% accuracy where only 2% of cases are positive. Why may accuracy mislead?

<details>
<summary>Answer key</summary>

1. (1/6).
2. (3/6=1/2).
3. (3/10=30\%\).
4. (45/200=22.5\%\). The deployment population or collection process may differ.
5. (1-0.37=0.63).
6. An always-negative model could achieve 98% accuracy while detecting no positive cases. Inspect recall, precision, class-specific errors, and error costs.

</details>

## 1.12 Revision card

- Probability quantifies uncertainty under stated assumptions.
- Classical formula: (P(A)=|A|/|S|), only for equally likely outcomes.
- Range: (0\le P(A)\le1).
- Complement: (P(A^c)=1-P(A)).
- First question: what exactly is the event, and what model justifies the calculation?

## References

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)
- [OpenStax, Introductory Statistics](https://openstax.org/details/books/introductory-statistics)

These are starting references; consult relevant sections when expanding the notes.
