# --------------- QUIZ 3 ---------------
'''
Try your best on this quiz! Partial credit will be given. 

Be sure to write tests for your code for full credit!
Example of a well written test:
    calc_sum(1, 2, 3)     # Expected output: 6
'''

# ---- Section 1: Strings/Conditionals -----

# PROBLEM 1
# Define a function called greet that takes in two strings, name and date, and returns
# a message for a computer's home screen.
# Ex: Given "Luke" and "12/7", return: "Hello Luke, today is 12/7."
# NOTE: This function below is incomplete! Make sure to give it appropriate arguments!
def greet() -> str:
    # Erase pass and write code here
    pass

# PROBLEM 2
# Create a new function, greet2, with the same inputs and outputs as greet, but only
# returns a message if the user's name is "Alice" or "Bob".
# Otherwise, it should return "Invalid user." Use greet (from Problem 1) as a helper
# function in your solution.


# PROBLEM 3
# Create a function that takes in two words and checks whether or not they start with
# the same letter.
# Make sure to label input/output types properly!


# ---- Section 2: Data Structures -----

# PROBLEM 4
jacket_prices = [55, 40, 35, 60, 70, 100, 90, 85, 95]
# You have a list of prices for jackets at a certain department store, but remembered
# that you have a $10 off coupon to use on any item.
#
# Define a function that takes in an arbitrary list (not necessarily the above list!)
# and subtracts 10 from each item's value.
#
# For example, if you pass in jacket_prices to your function, it should return [45, 30, 25, etc.]


# Refer to the temps dictionary below for the next two problems.
# This represents the daily temperature forecasts for various cities over the next week
temps = {"Boston": [43, 42, 34, 47, 48, 47, 51], "San Francisco": [
    58, 60, 59, 61, 63, 59, 60], "Miami": [76, 76, 75, 73, 74, 76, 72]}

# PROBLEM 5
# What data type are the keys of this dictionary? What data type are the values?


# PROBLEM 6
# Use average() and the temperatures to find the average temperature over the next week,
# in Boston, Miami, and SF.
# Reassign the variables below accordingly: avg_boston_temp should be equal to the average
# temperature of the Boston forecast, for example.
# Remember: you can access values from a dictionary by using square bracket notation!

# Returns the average/mean value of a list of numbers.
def average(a_list: list) -> float:
    return sum(a_list) / len(a_list)

avg_boston_temp = None
avg_sf_temp = None
avg_miami_temp = None


'''
---- CHALLENGE PROBLEM -----
Try solve this problem if you are finished with the quiz early! 
It is worth *NO POINTS, but do it if you want a challenge.

*but it might be extra credit... ;)
'''

# Word Frequency Counter
#
# Write a Python function that takes a text string as input and returns a dictionary
# containing the frequency of each word in the text.
# The program should ignore punctuation, be case-insensitive, and handle common words
# (e.g., "the", "and", "is") as well.
# The following might be useful:
# my_str = "Rebecca"
# my_str.lower()    --> "rebecca"

# my_sentence = "hello here is a little sentence"
# my_sentence.split()    --> ["hello", "here", "is", "a", "little", "sentence"]
