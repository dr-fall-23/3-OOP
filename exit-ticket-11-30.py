from typing import List, Dict
# EXIT TICKET 11/30
# During tomorrow's Hackathon you're going to put your coding skills to the test!
# Let's make sure you remember how to use lists, dictionaries, and classes. These data structures
# are critical for building large programs (like video games)
# As always, you can use your notes and slides from lecture!

# QUESTION 1
november_temps = [42, 50, 44, 40, 33, 36, 31, 39, 29, 35]
# Above are some temperatures collected in Boston during November, in Farenheight.

# Write a function called check_temp that takes in a list (not necessarily this one!), and prints
# out "brrr" every time it's below freezing (32)


# QUESTION 2
my_dict = {"Bananas": 3, "Oranges": 10, "Apples": 2, "Pears": 5}
# I have a grocery list above, represented as a dictionary, with the keys being types of produce
# and the values being the quantity I want to buy.
# BUT! I just realized two things: I actually don't want any apples, and I do want extra bananas.

# Using square bracket notation, change the quantity of bananas to 5, and the quantity of apples to 0.


# QUESTION 3
class Person:
    def __init__(self, name: str, age: int, has_pet: bool) -> None:
        self.name = name
        self.age = age
        self.has_pet = has_pet

    def can_vote(self):
        return self.age >= 18

# Create an instance of the Person class, with whatever attributes you want.
# Then, create a method in the Person class called can_vote, and returns True if and only if this Person is 18 or older
