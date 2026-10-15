# Probability Foundations: Events, Complements, OR, AND and Conditional Probability

**Learning objective:** Translate a word problem into outcomes and events, choose the correct probability rule, and calculate the answer with confidence.

**Prerequisites:** Fractions, percentages, and basic set notation.  
**Status:** In progress — introductory conditional-probability practice completed; full topic review pending.

## 1. What probability means

Probability measures how likely an event is. It ranges from 0 to 1:
- (0): impossible;
- (1): certain;
- values between 0 and 1: varying degrees of likelihood.

For equally likely outcomes,

[
P(A)=\frac{\text{number of outcomes in }A}{\text{total number of possible outcomes}}.
]

For example, a fair coin has two equally likely outcomes, heads and tails. The probability of heads is (1/2). This shortcut applies only when the outcomes being counted are equally likely.

## 2. Sample space and events

The **sample space** (S) is the set of all possible outcomes. An **event** is a set of outcomes of interest.

For one fair six-sided die,

[
S=\{1,2,3,4,5,6\}.
]

Let (A) be “the result is even.” Then (A=\{2,4,6\}), so (P(A)=3/6=1/2).

Writing the set first prevents a common mistake: counting outcomes that do not satisfy the event.

## 3. Complement: “not A”

The complement (A^c) contains all outcomes in the sample space that are not in (A).

[
P(A^c)=1-P(A).
]

**Example:** The probability of rolling a 6 is (1/6). Therefore, the probability of not rolling a 6 is (1-1/6=5/6).

**Useful clue words:** not, does not, none, at least one (often solved by subtracting the probability of none from 1).

## 4. OR rule: (A\cup B)

“(A) or (B)” means that at least one event occurs. If both events can occur together, their overlap must not be counted twice.

[
P(A\cup B)=P(A)+P(B)-P(A\cap B).
]

Here (A\cap B) means outcomes belonging to both events.

**Example:** Roll a fair die. Let (A=\{2,4,6\}) be even and (B=\{5,6\}) be greater than 4.

- (A\cup B=\{2,4,5,6\}), with 4 outcomes.
- The overlap is (A\cap B=\{6\}), with 1 outcome.

Thus (P(A\cup B)=3/6+2/6-1/6=4/6=2/3).

If events cannot overlap, (P(A\cap B)=0), and the OR rule reduces to (P(A\cup B)=P(A)+P(B)).

## 5. AND rule: (A\cap B)

“(A) and (B)” means both events occur. The general multiplication rule is

[
P(A\cap B)=P(A)P(B\mid A),
]

provided the conditional probability is defined. If the events are independent, knowing that (A) occurred does not change the probability of (B), so

[
P(A\cap B)=P(A)P(B).
]

**Example:** Toss a fair coin twice. The tosses are independent. The probability of heads on both tosses is (1/2\times1/2=1/4).

Do not multiply probabilities automatically: first check whether independence is given or justified.

## 6. Conditional probability: “given that”

Conditional probability answers a question after some information is known. The condition restricts which outcomes remain possible.

[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0.
]

For equally likely outcomes, this becomes

[
P(A\mid B)=\frac{\text{outcomes satisfying both }A\text{ and }B}
{\text{outcomes satisfying }B}.
]

**Example:** A fair die is rolled. Given that the result is greater than 3, find the probability that it is even.

1. The condition “greater than 3” restricts the sample space to (\{4,5,6\}).
2. The even outcomes within this restricted set are (\{4,6\}).
3. There are 2 favourable outcomes out of 3 allowed outcomes, so the probability is (2/3).

**Most important habit:** Apply the condition first. Do not keep using the original sample-space size after the question has restricted it.

## 7. A practical decision guide

| Wording in the question | First action | Rule |
|---|---|---|
| “not A” | Find the complement | (1-P(A)) |
| “A or B” | Check whether they overlap | Addition rule |
| “A and B” | Check dependence/independence | Multiplication rule |
| “given B” | Restrict to outcomes where B is true | Conditional probability |
| “at least one” | Consider the complement “none” | Often (1-P(\text{none})) |

## 8. Common errors to avoid

1. Using the original total after a condition has restricted the sample space.
2. Adding (P(A)) and (P(B)) without subtracting their overlap.
3. Multiplying probabilities without checking independence.
4. Confusing (P(A\mid B)) with (P(B\mid A)); these are generally different.
5. Treating equally likely outcome counting as valid when outcomes have different probabilities.

## 9. Short worked examples

### Example A — Complement
A machine has probability (0.08) of failing during a test. If failure and no failure are the only possibilities, the probability of no failure is (1-0.08=0.92).

### Example B — OR with overlap
A card is drawn from a standard 52-card deck. Let (A) be “heart” and (B) be “king.” There are 13 hearts, 4 kings, and one card that is both (king of hearts). Therefore,

[
P(A\cup B)=\frac{13}{52}+\frac{4}{52}-\frac{1}{52}=\frac{16}{52}=\frac{4}{13}.
]

### Example C — Conditional probability
In a group of 20 devices, 8 are laptops and 5 of those laptops have a particular feature. Given that a selected device is a laptop, the probability it has the feature is (5/8). The denominator is the laptop group, not all 20 devices.

## 10. Topic checklist

Before moving on, a learner should be able to:
- define a sample space and an event;
- calculate probability by counting equally likely outcomes;
- use the complement rule;
- apply the OR rule and account for overlap;
- distinguish AND from OR and use the multiplication rule correctly;
- solve conditional-probability problems by restricting the sample space;
- explain why the denominator changes when a condition is given.

## 11. Practice policy

The course uses a maximum of five questions per topic by default, extending to ten only when the topic genuinely requires more coverage. Questions progress from easy to challenging. Uploaded assignment questions are reference material: lessons use different numbers and contexts, and assignment solutions are not disclosed unless requested separately.

## Further study
- [Probability and statistics roadmap](../README.md)
- [MFCS assignment index](../assignments/README.md)
- [Teaching protocol](../teaching-protocol.md)
