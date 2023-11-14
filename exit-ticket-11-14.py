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


# CHALLENGE QUESTION
# This will not count against your grade, so give it your best go!
# Given a list nums, for each number find out how many other numbers are smaller than it, and return all of the answers in a list.
# For example: [8, 1, 2, 2, 3] should return [4, 0, 1, 1, 3] since 8 has 4 numbers less than it, 1 has 0 numbers less than it, 2 has 1 number less than it, etc
# (Hint: you will need multiple loops)
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    # Erase pass and write your code here!
    pass


print(smallerNumbersThanCurrent[8, 1, 2, 2, 3])        # should output [4, 0, 1, 1, 3]
print(smallerNumbersThanCurrent[6, 5, 4, 8])            # should output [2, 1, 0, 3]
print(smallerNumbersThanCurrent[7, 7, 7, 7])            # should output [0, 0, 0, 0]
