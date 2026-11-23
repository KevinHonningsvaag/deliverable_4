from __future__ import annotations

TEMPRATURE_TOLERANCE = 1e-9
VALID_UNITS = ["K", "C", "F"]


class Temprature:
    def __init__(self, value: float, unit: str = "C") -> None:

        self._value = value
        self._unit = unit.upper()

        if self._unit not in VALID_UNITS:
            raise ValueError("Unit needs to be kelvin, celsius or fahrenheit")

        if self.to_kelvin() < -TEMPRATURE_TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    def to_celsius(self) -> float:
        """Calculate respective unit into celsius"""
        if self._unit == "K":
            return self._value - 273.15
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value  # Returns if the unit is already celsius

    def to_kelvin(self) -> float:
        """Calculate respective unit into Kelvin"""
        if self._unit == "C":
            return self._value + 273.15
        elif self._unit == "F":
            return self.to_celsius() + 273.15
        return self._value  # Returns if the unit is already kelvin

    def to_fahrenheit(self) -> float:
        """Calculate respective unit into fahrenheit"""
        if self._unit == "C":
            return self._value * 9 / 5 + 32
        elif self._unit == "K":
            return self.to_celsius() * 9 / 5 + 32
        return self._value  # Returns if the uniit is already fahrenheit

    def convert_to(self, target_unit: str) -> Temprature:
        """Uses the convert to methods and the given target unit, gives a temprature with a value and unit"""
        if target_unit == "C":
            return Temprature(self.to_celsius(), target_unit)
        elif target_unit == "F":
            return Temprature(self.to_fahrenheit(), target_unit)
        elif target_unit == "K":
            return Temprature(self.to_kelvin(), target_unit)
        return Temprature(self._value, self._unit)  # Returns if the target unit is already the unit
