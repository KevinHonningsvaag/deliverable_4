from __future__ import annotations

from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize a fraction with a numerator and denominator.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int): The denominator of the fraction.

        Raises:
            TypeError: If numerator or denominator is not an integer.
            ValueError: If denominator is not positive.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int): # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("Numerator and denominator must be integers")

        if denominator <= 0:
            raise ValueError("Denominator must be positive and more than zero")

        # Find the greatest common divisor
        divisor = gcd(numerator, denominator)

        # Simplify the fraction
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __eq__(self, other: object) -> bool:
        """Returns True if two fractions are equal"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other: object) -> bool:
        """Returns true if two fractions are unequal"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool:
        """Checks if self is less than other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other: object) -> bool:
        """Checks if self is greater than other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other: object) -> bool:
        """Checks if self is less or equal to other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ge__(self, other: object) -> bool:
        """Checks if self is gretaer or equal to other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __add__(self, other: object) -> Fraction:
        """Adds two fractions together"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            ((self.numerator * other.denominator) + (other.numerator * self.denominator)),
            (self.denominator * other.denominator),
        )

    def __sub__(self, other: object) -> Fraction:
        """Subtracts one fraction from the other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            ((self.numerator * other.denominator) - (other.numerator * self.denominator)),
            (self.denominator * other.denominator),
        )

    def __mul__(self, other: object) -> Fraction:
        """multiplies two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: object) -> Fraction:
        """DIvides two fractions"""
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        if other.numerator == 0:
            raise ZeroDivisionError

        if other.numerator < 0:
            new_numerator = new_numerator * -1
            new_denominator = new_denominator * -1

        return Fraction(new_numerator, new_denominator)
