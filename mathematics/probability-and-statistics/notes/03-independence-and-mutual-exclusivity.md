# Independence, Dependence, and Mutually Exclusive Events

> Mathematical Foundations of Computer Science · Probability and Statistics · Concept notes and worked examples

## Learning objectives
After studying this chapter, a reader should be able to distinguish independent, dependent, and mutually exclusive events; calculate intersections using conditional probabilities; test independence numerically; and explain why disjoint non-impossible events cannot be independent.

## 1. Prerequisites and notation
For events A and B in sample space S:
- P(A): probability A occurs.
- P(A ∩ B): probability both occur.
- P(A ∪ B): probability at least one occurs.
- P(B | A): probability B occurs given that A has occurred, defined when P(A)>0.

Conditional probability: **P(B | A) = P(A ∩ B) / P(A)**.

## 2. Independent events
Events A and B are independent when learning that A occurred does not change the probability of B.

**Definition:** P(A ∩ B) = P(A)P(B).

When P(A)>0, this is equivalent to P(B | A)=P(B). Independence is symmetric.

### Worked example: two independent requests
Suppose two independently handled requests each have a 0.1 probability of timing out. Let A be the first timeout and B the second timeout.
- P(A ∩ B)=0.1 × 0.1=0.01.
- P(at least one timeout)=0.1+0.1−0.01=0.19.
- P(no timeout)=0.9 × 0.9=0.81.

**Important assumption:** Separate requests are not automatically independent. Shared server outages, rate limits, or network failures can correlate their outcomes. The arithmetic is valid only under the stated independence assumption.

### Worked example: draws with replacement
A bag has 4 red and 6 blue balls. Draw a ball, replace it, mix, and draw again.
P(red on second | red on first)=4/10, equal to P(red on second)=4/10.
P(both red)=(4/10)(4/10)=4/25.

## 3. Dependent events
Events are dependent if information about one changes the probability of the other.

**General multiplication rule:** P(A ∩ B)=P(A)P(B | A).

### Worked example: draws without replacement
The same bag has 4 red and 6 blue balls. Draw two balls without replacement.
- P(first red)=4/10.
- P(second red | first red)=3/9.
- P(both red)=(4/10)(3/9)=2/15.

Because 3/9 differs from the initial red probability 4/10, the draws are dependent.

### Software example: shared infrastructure
Two services hosted on the same server may both fail when the server goes down. Observing failure of one can raise the probability of failure of the other. Treating these failures as independent without evidence underestimates joint risk.

## 4. Mutually exclusive events
Events A and B are mutually exclusive (disjoint) if they cannot occur in the same trial.

**Definition:** P(A ∩ B)=0.

### Worked example: one die roll
A={1,3,5} (odd); B={2,4,6} (even). They have no shared outcome.
- P(A ∩ B)=0.
- P(A ∪ B)=P(A)+P(B)=1.

For any events, the general addition rule is **P(A ∪ B)=P(A)+P(B)−P(A ∩ B)**.

## 5. Why mutually exclusive is not independent
If P(A)>0 and P(B)>0, independent events require P(A ∩ B)=P(A)P(B)>0. But mutually exclusive events require P(A ∩ B)=0. Thus events with positive probability cannot be both mutually exclusive and independent.

The special exception is when at least one event has probability zero.

### Overlapping does not guarantee independence
For a fair die:
- A={2,4,6} (even), P(A)=1/2.
- B={4,5,6} (greater than 3), P(B)=1/2.
- A ∩ B={4,6}, P(A ∩ B)=1/3.
Since 1/3 ≠ (1/2)(1/2)=1/4, the events overlap but are dependent.

## 6. Numerical independence test
Suppose P(A)=0.4, P(B)=0.5, and P(A ∩ B)=0.2.
P(A)P(B)=0.4 × 0.5=0.2. Therefore A and B are independent.

If the intersection were 0.15 instead, they would be dependent.

## 7. Decision checklist
1. Can both events happen in the same trial? If no, they are mutually exclusive.
2. Does P(A ∩ B) equal P(A)P(B)? If yes, they are independent.
3. If conditional information is provided, compare P(B | A) with P(B).
4. For successive draws, check whether replacement restores the original composition.
5. Do not infer independence from separate labels, separate systems, or an absence of obvious causation.

## 8. Formula sheet
| Concept | Formula |
| --- | --- |
| Conditional probability | P(B | A)=P(A ∩ B)/P(A), P(A)>0 |
| General intersection | P(A ∩ B)=P(A)P(B | A) |
| Independence | P(A ∩ B)=P(A)P(B) |
| Mutually exclusive | P(A ∩ B)=0 |
| General union | P(A ∪ B)=P(A)+P(B)−P(A ∩ B) |
| Disjoint union | P(A ∪ B)=P(A)+P(B) |

## 9. Practice problems (no solutions)
1. A bag contains 4 red and 6 blue balls. Two draws are made with replacement. Are the events 'first red' and 'second red' independent? Explain.
2. Repeat Problem 1 without replacement. Calculate the probability both draws are red.
3. One fair die is rolled. A='even', B='greater than 4'. Are these events mutually exclusive? Are they independent? Show the intersection calculation.
4. Given P(A)=0.3, P(B)=0.6, and P(A ∩ B)=0.18, determine whether A and B are independent.
5. Two software components share a database. Explain why a shared database outage can make their failures dependent, and state what data would be needed to test independence.

## 10. Common mistakes
- Assuming 'mutually exclusive' and 'independent' mean the same thing.
- Multiplying P(A)P(B) without first establishing independence.
- Forgetting that without-replacement draws change the sample space.
- Confusing P(A ∩ B) ('both') with P(A ∪ B) ('at least one').
- Assuming causation is required for statistical dependence.

**Study status:** Reference notes prepared. Mastery must be assessed separately through practice; publication does not indicate completion.
