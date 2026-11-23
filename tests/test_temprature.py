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
