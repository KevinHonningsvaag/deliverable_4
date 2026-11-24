from deliverable_4.fraction import Fraction

import pytest


def test_initialization():
    fraction = Fraction(12, 18)

    assert fraction.numerator == 2
    assert fraction.denominator == 3


def test_invalid_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(1, -3)


def test_invalid_types():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    with pytest.raises(TypeError):
        Fraction(1, "3")


def test_equality():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 4)
    fraction3 = Fraction(3, 4)

    assert fraction1 == fraction2
    assert fraction1 != fraction3

    assert (fraction1 == fraction3) is False
    assert (fraction1 != fraction2) is False


def test_comparison():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)

    assert fraction1 < fraction2
    assert fraction2 > fraction1
    assert fraction1 <= fraction2
    assert fraction2 >= fraction1

    assert (fraction1 > fraction2) is False

    fraction3 = Fraction(2, 4)

    assert fraction1 <= fraction3
    assert fraction1 >= fraction3


def test_addition():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(1, 4)

    assert fraction1 + fraction2 == Fraction(3, 4)


def test_difference():
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(1, 2)

    assert fraction1 - fraction2 == Fraction(1, 4)


def test_multiplication():
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(3, 4)

    assert fraction1 * fraction2 == Fraction(1, 2)


def test_division():
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(2, 5)

    assert fraction1 / fraction2 == Fraction(15, 8)


def test_division_by_zero():
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(0, 5)

    with pytest.raises(ZeroDivisionError):
        fraction1 / fraction2


def test_negative_division():
    """Test division with negative fractions."""
    positive = Fraction(2, 3)
    negative = Fraction(-4, 5)

    assert positive / negative == Fraction(-5, 6)
    assert negative / positive == Fraction(-6, 5)
    assert negative / negative == Fraction(1, 1)


def test_zero_numerator():
    """Test simplification with a zero numerator."""
    fraction = Fraction(0, 5)

    assert fraction.numerator == 0
    assert fraction.denominator == 1


def test_zero_over_zero():
    """Test that a zero denominator raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(0, 0)


def test_false_comparisons():
    """Test false outcomes of comparison operators."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)

    assert (fraction2 < fraction1) is False
    assert (fraction1 > fraction2) is False
    assert (fraction2 <= fraction1) is False
    assert (fraction1 >= fraction2) is False


def test_unsupported_types():
    """Test operations with unsupported object types."""
    fraction = Fraction(1, 2)

    assert fraction.__eq__("hello") is NotImplemented
    assert fraction.__ne__(3) is NotImplemented
    assert fraction.__lt__(3) is NotImplemented
    assert fraction.__le__(3) is NotImplemented
    assert fraction.__gt__(3) is NotImplemented
    assert fraction.__ge__(3) is NotImplemented

    with pytest.raises(TypeError):
        fraction + 3

    with pytest.raises(TypeError):
        fraction - 3

    with pytest.raises(TypeError):
        fraction * 3

    with pytest.raises(TypeError):
        fraction / 3


def test_unchanged_fractions():
    """Test that arithmetic does not modify original fractions."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(1, 3)

    fraction1 + fraction2
    fraction1 - fraction2
    fraction1 * fraction2
    fraction1 / fraction2

    assert fraction1.numerator == 1
    assert fraction1.denominator == 2
    assert fraction2.numerator == 1
    assert fraction2.denominator == 3
