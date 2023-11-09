from typing import List

# QUESTION 1
# Write a class called Person that has two attibutes: name and fav_color (both strings!)
# NOTE: We've given you an incomplete constructor - fill in the arguments and the function body
class Person:
    def __init__(self) -> None:
        pass


# QUESTION 2
# Set the variable luke equal to a Person object, using the syntax from the slides
# Give this Person object the name "Luke", and whatever favorite color you think Luke would like.
luke = None

# Bonus: repeat the above for all the other staff members!
# (This is the benefit of classes: it gives us a template which we can reuse)


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
