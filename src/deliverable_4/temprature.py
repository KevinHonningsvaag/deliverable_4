from __future__ import annotations

TEMPRATURE_TOLERANCE = 1e-9
VALID_UNITS = ["K", "C", "F"]


class Temprature:
    """Represents a temprature"""

    def __init__(self, value: float, unit: str = "C") -> None:
        """
        Args:
           value (float): the temprature
           unit (str): what unit the temprature is in, acepted units(Kelvin, celsius and fahrenheit)
        """
        self._value = value
        self._unit = unit.upper()

        if self._unit not in VALID_UNITS:
            raise ValueError("Unit needs to be kelvin, celsius or fahrenheit")

        if self.to_kelvin() < -TEMPRATURE_TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        """Public read only property to inspect value"""
        return self._value

    @property
    def unit(self) -> str:
        """Public read only property to inspect value"""
        return self._unit

    def __str__(self) -> str:
        """String representation of temprature"""
        return f"{self._value:.2f} °{self._unit}"

    def __repr__(self) -> str:
        """Representation of temprature"""
        return f"{type(self).__name__}({self._value!r}, {self._unit!r})"

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

    def _difference(self, other: Temprature) -> float:
        """Finds the difference betwen to temperatures, treating differences within the tolerance as no difference"""
        temprature_1 = self.to_kelvin()
        temprature_2 = other.to_kelvin()
        if temprature_1 == temprature_2:
            return 0.0
        difference = temprature_1 - temprature_2
        return 0.0 if abs(difference) <= TEMPRATURE_TOLERANCE else difference

    def __eq__(self, other: object) -> bool:
        """Checks if two temperatures is equal"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) == 0

    def __ne__(self, other: object) -> bool:
        """Checks if two temperatures are unequal"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) != 0

    def __lt__(self, other: object) -> bool:
        """Checks if the first temperature is lower than the second"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) < 0

    def __le__(self, other: object) -> bool:
        """Checks if the first temperature is lower than or equal to the second"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) <= 0

    def __gt__(self, other: object) -> bool:
        """Checks if the first temperature is higher than the second"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) > 0

    def __ge__(self, other: object) -> bool:
        """Checks if the first temperature is higher than or equal to the second"""
        if not isinstance(other, Temprature):
            return NotImplemented
        return self._difference(other) >= 0
