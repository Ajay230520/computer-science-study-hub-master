# Exercises: Probability Foundations

Solve these without looking at the notes. Show the sample space/event when practical and state assumptions.

## Easy
1. A fair coin is tossed once. Find the probability of tails.
2. Roll a fair six-sided die. Find the probability of a number less than 3.
3. A jar has 4 green and 6 yellow marbles. One marble is drawn uniformly. Find the probability of green.

## Intermediate
4. A fair die is rolled. What is the probability of not rolling a 6? Solve using counting and the complement rule.
5. In a batch of 250 components, 15 are defective. One component is selected uniformly. Find the probability it is defective. What does this say—and not say—about next month's production?
6. A dataset contains 75 positive examples and 425 negative examples. Calculate the positive proportion. Give one reason it could differ from production traffic.

## Challenge
7. A classifier is evaluated on 10,000 cases, of which 1% are truly positive. It predicts every case as negative. Calculate accuracy and recall. Explain why these metrics tell different stories.
8. Explain why counting favorable outcomes is not enough when outcomes have unequal probabilities.

## Answers (check after trying)
1. (1/2).
2. ({1,2}) are favorable: (2/6=1/3).
3. (4/(4+6)=0.4=40\%\).
4. (5/6); complement: (1-P(6)=1-1/6=5/6).
5. (15/250=0.06=6\%\). This describes uniform sampling from that batch; future rates need a process/population assumption.
6. (75/(75+425)=0.15=15\%\). Sampling and production prevalence can differ.
7. Accuracy = 99%; recall = 0%, because no positive case is detected.
8. For unequal probabilities, add probabilities of favorable outcomes; raw counts weight outcomes incorrectly.
