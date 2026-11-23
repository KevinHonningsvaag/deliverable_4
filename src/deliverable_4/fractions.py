class Fraction:
    def __init__(self, numerator: int, denominator: int)-> None:
        self.numerator = numerator
        self.denominator = denominator
        if denominator <= 0:
            raise ValueError("Denominator must be positive and more than zero")
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")

        
