from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int)-> None:
        """Initialize a fraction with a numerator and denominator.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int): The denominator of the fraction.

        Raises:
            TypeError: If numerator or denominator is not an integer.
            ValueError: If denominator is not positive.
        """
        self.numerator = numerator
        self.denominator = denominator
        
        # Find the greatest common divisor
        divisor = gcd(numerator, denominator)

        # Simplify the fraction
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor
        if denominator <= 0:
            raise ValueError("Denominator must be positive and more than zero")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")

    def __eq__(self, other: object )-> bool:
        """Returns True if two fractions are equal"""
        if not isinstance(other, Fraction):
            return NotImplemented
        if self.numerator * other.denominator == self.denominator * other.numerator:
            return True
        else:
            return False

    def __ne__(self, other: object)-> bool:
        """Returns true if two fractions are unequal"""
        if not isinstance(other, Fraction):
                    return NotImplemented
        return not self.__eq__(other)
    

    def __lt__(self, other: object) -> bool:
        """ Checks if self is less than other """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator


    def __gt__(self, other: object) -> bool:
        """Checks if self is greater than other"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other: object) -> bool:
        """ Checks if self is less or equal to other """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= self.denominator * other.numerator      

    def __ge__(self, other: object) -> bool:
        """ Checks if self is gretaer or equal to other """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= self.denominator * other.numerator   

    def __add__(self, other: object) -> Fraction:
        """Adds two fractions together"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction((
            (self.numerator * other.denominator)
            + (other.numerator * self.denominator)),
            (self.denominator * other.denominator))