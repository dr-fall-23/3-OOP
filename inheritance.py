class Car:
    def __init__(self, color, model, year) -> None:
        self.color = color
        self.model = model
        self.year = year


class Plane:
    def __init__(self, color, model, year, max_altitude) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.max_altitude = max_altitude


class Boat:
    def __init__(self, color, model, year, propulsion) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.propulsion_type = propulsion
