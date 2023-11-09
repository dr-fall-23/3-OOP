# ---------- QUIZ 2 (Take Home) ----------
# NOTE: This quiz is meant to test your understanding before we move on to more advanced concepts in this course.
# Try your best! If you make mistakes, then course staff can help you learn, so that for the later parts of the
# course that build upon these concepts, you can do better!

'''
For each problem:
1) Write out an English explanation of your thought process (1-2 sentences)
2) Write tests for the function
3) Write your actual code

All three (3) of these contribute to your grade!!!
'''


# Problem 1
# Define a function "is_even_length" that takes in two strings and returns "even" if the strings' combined
# length is even, and returns "odd" if the strings' combined length is odd


# Problem 2
# In Rock Paper Scissors Shovel Snake (a variation of Rock Paper Scissors), Shovel always wins, and Snake always
# loses. Write a function "rps2" which takes in 2 players moves (one of: "rock", "paper", "scissors", "shovel", "snake")
# and returns the winning move, or "draw". We are giving you the original rps function to be used as a helper function
# in your answer.


def rps(player1: str, player2: str) -> str:
    if (player1 == player2):
        return "draw"
    elif ((player1 == "rock" and player2 == "scissors")
          or (player1 == "scissors" and player2 == "paper")
          or (player1 == "paper" and player2 == "rock")):
        return player1
    else:
        return player2


# Problem 3
# Python has a "max" function, which takes in a list of positive numbers and returns the largest number within.
# Recreate the max function (call it "max2").


# Problem 4
# Write a function, "even_product", which is given a list of integers, and returns the result of multiplying
# all even numbers in the list together.


# Problem 5
# As a teacher, Ms. Frizzle keeps track of her students scores in a dictionary.
# Here is an example of how she keeps track of the scores:
student_scores_1 = {
    "Alice": [85, 70, 42, 60],
    "Bob": [92, 91, 95, 0],
    "Charlie": [78, 80, 85, 95],
    "David": [90, 88, 92, 85],
    "Eva": [88, 99, 93, 94]
}
# Ms. Frizzle wants to get and understanding of how well her students are doing on average.
# Write a function, "calculate_average_score" that returns just one number representing how well her
# students are doing on average. For example, maybe on average her class has a 82.

# The following average function is provided as a helper function


def average(li: List[int]) -> float:
    return sum(li) / len(li)
