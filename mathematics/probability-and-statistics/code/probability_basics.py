"""Beginner probability demonstrations for the Computer Science Study Hub.

Run:
    python probability_basics.py

Uses exact finite counting; assumes all listed outcomes are equally likely.
"""
from fractions import Fraction


def classical_probability(favorable: int, total: int) -> Fraction:
    """Return favorable/total after validating a finite counting model."""
    if total <= 0:
        raise ValueError("total must be positive")
    if favorable < 0 or favorable > total:
        raise ValueError("favorable must be between 0 and total")
    return Fraction(favorable, total)


def main() -> None:
    examples = [
        ("Heads in a fair coin toss", 1, 2),
        ("Number greater than 4 on a fair die", 2, 6),
        ("Defective sensor from a batch of 100 with 8 defective", 8, 100),
        ("Cracked-road class proportion in 1,000 images, 120 positive", 120, 1000),
    ]

    for label, favorable, total in examples:
        probability = classical_probability(favorable, total)
        print(f"{label}: {probability} = {float(probability):.4f} "
              f"({float(probability) * 100:.2f}%)")

    p_late = 0.07
    print(f"Not-late complement when P(late)=0.07: {1 - p_late:.2f} (93.00%)")


if __name__ == "__main__":
    main()
