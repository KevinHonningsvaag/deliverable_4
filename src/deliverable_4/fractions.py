class Fraction:
    def __init__(self, numerator: int, denominator: int)-> None:
        """ Initialiser"""
        self.numerator = numerator
        self.denominator = denominator
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
        
