from typing import List

# QUESTION 1
# You have the class Car as seen below.
#
# Reassign the variable cool_car to a Car object that represents a red 2016 Prius
# Then, access the model of that car using dot notation from the lecture today


class Car:
    def __init__(self, year: int, model: str, color: str) -> None:
        self.year = year
        self.model = model
        self.color = color


cool_car = None


# QUESTION 2
# Write a method paint() that changes the car's color to whatever you give it.
# Ex. my_car.paint("green") should change the color of my_car to "green"
# Then, change the color of cool_car to whatever your favorite color is!
# NOTE: this method returns None!! It just "mutates" your Car object
