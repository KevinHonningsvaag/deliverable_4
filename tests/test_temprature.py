import pytest

from deliverable_4.temprature import Temprature


def test_default_unit_is_celsius() -> None:
    temperature = Temprature(21)
    assert temperature.value == 21
    assert temperature.unit == "C"


@pytest.mark.parametrize("unit", ["c", "C", "f", "F", "k", "K"])
def test_units_are_case_insensitive(unit: str) -> None:
    temperature = Temprature(21, unit)
    assert temperature.unit == unit.upper()
    assert temperature.value == 21


@pytest.mark.parametrize(("attribute", "new_value"), [("value", 30.0), ("unit", "K")])
def test_attributes_are_read_only(attribute: str, new_value: float | str) -> None:
    temperature = Temprature(21, "C")
    with pytest.raises(AttributeError):
        setattr(temperature, attribute, new_value)


@pytest.mark.parametrize("unit", ["", "X", "Kelvin"])
def test_invalid_unit_raises_value_error(unit: str) -> None:
    with pytest.raises(ValueError):
        Temprature(21, unit)


@pytest.mark.parametrize(("value", "unit"), [(-273.16, "C"), (-459.68, "F"), (-0.01, "K")])
def test_below_absolute_zero_raises_value_error(value: float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temprature(value, unit)


@pytest.mark.parametrize(("value", "unit"), [(-273.15, "C"), (-459.67, "F"), (0.0, "K")])
def test_absolute_zero_is_valid(value: float, unit: str) -> None:
    temperature = Temprature(value, unit)
    assert temperature.value == value


@pytest.mark.parametrize(
    ("celsius", "fahrenheit", "kelvin"),
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (37.0, 98.6, 310.15),
        (100.0, 212.0, 373.15),
    ],
    ids=["absolute-zero", "crossover", "freezing", "body-temperature", "boiling"],
)
@pytest.mark.parametrize("unit", ["C", "F", "K"])
def test_reference_conversions(celsius: float, fahrenheit: float, kelvin: float, unit: str) -> None:
    values = {"C": celsius, "F": fahrenheit, "K": kelvin}
    temperature = Temprature(values[unit], unit)
    assert temperature.to_celsius() == pytest.approx(celsius, abs=1e-9)
    assert temperature.to_fahrenheit() == pytest.approx(fahrenheit, abs=1e-9)
    assert temperature.to_kelvin() == pytest.approx(kelvin, abs=1e-9)


def test_round_trip_conversion() -> None:
    original = Temprature(37.0, "C")
    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    result = kelvin.convert_to("C")

    assert (fahrenheit.unit, kelvin.unit, result.unit) == ("F", "K", "C")
    assert fahrenheit.value == pytest.approx(98.6, abs=1e-9)
    assert kelvin.value == pytest.approx(310.15, abs=1e-9)
    assert result.value == pytest.approx(original.value, abs=1e-9)


@pytest.mark.parametrize(
    ("fahrenheit", "kelvin", "order"),
    [(32.0, 273.15, 0), (32.0, 273.15 + 5e-10, 0), (32.0, 274.15, -1), (32.0, 272.15, 1)],
    ids=["equal", "within-tolerance", "colder", "warmer"],
)
def test_cross_unit_comparisons(fahrenheit: float, kelvin: float, order: int) -> None:
    first = Temprature(fahrenheit, "F")
    second = Temprature(kelvin, "K")
    assert (first == second) == (order == 0)
    assert (first != second) == (order != 0)
    assert (first < second) == (order < 0)
    assert (first <= second) == (order <= 0)
    assert (first > second) == (order > 0)
    assert (first >= second) == (order >= 0)


@pytest.mark.parametrize(
    ("value", "unit", "expected"),
    [(25.0, "C", "25.00 °C"), (-40.126, "F", "-40.13 °F"), (0.0, "K", "0.00 °K")],
)
def test_str_format(value: float, unit: str, expected: str) -> None:
    assert str(Temprature(value, unit)) == expected


def test_repr_format() -> None:
    assert repr(Temprature(25.125, "c")) == "Temprature(25.125, 'C')"
