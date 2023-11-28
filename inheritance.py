# Represents a motorized car with a distinct color, model, and year it was made
class Car:
    def __init__(self, color: str, model: str, year: int) -> None:
        self.color = color
        self.model = model
        self.year = year


# Represents a motorized plane with a distinct color, model, year, and maximum altitude (in ft)
class Plane:
    def __init__(self, color: str, model: str, year: int, max_altitude: int) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.max_altitude = max_altitude


# Represents a boat with a color, model, year, and type of propulsion
class Boat:
    def __init__(self, color: str, model: str, year: int, propulsion: str) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.propulsion_type = propulsion
