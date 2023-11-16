# --------- EXIT TICKET 11/16 ---------
# We've given you some starter code for a Triangle class.

# QUESTION 1
# Write the constructor (aka __init__())
# A Triangle should have two fields: base and height (representing the length of the base and the length of the height, respectively)

# QUESTION 2
# Write the calc_area() method that calculates the area of this triangle
# A triangle's area is (1/2) * base * height

# QUESTION 3
# Complete the bigger_area_than() method.
# Refer to your notes from today for help!


class Triangle:

    # Returns whether or not this circle has a bigger area than another triangle
    def bigger_area_than(self, other_triangle: 'Triangle') -> bool:
        # Write your code here!
        pass


my_triangle_1 = Triangle(2, 5)
my_triangle_2 = Triangle(1, 8)


# CHALLENGE QUESTION
#
# Create a class called Node that takes has a field called value, with type int,
# and another field called next, with type 'Node'
#
# We can think of this as an entry in a list, with a 'link' (self.next) to the next entry
#
# Then, write a single Node object to represent the following list: [1, 2, 3]
class Node:
    # Write your constructor here
    pass


my_node = None      # Reassign this variable!


# You should be able to plug my_node into this function, and get the number 6
def sum_linked_list(single_node: Node) -> int:
    if single_node.next is None:
        return single_node.value
    return single_node.value + sum_linked_list(single_node.next)


print(sum_linked_list(my_node))
