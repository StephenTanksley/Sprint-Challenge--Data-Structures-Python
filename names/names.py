import time
from collections import Counter

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Take the current value of our node
        # Compare to the new value we want to insert.
        new_node = BSTNode(value)

        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        # If the value of the node is greater than the target:
        elif self.value > target:
            # Check to see if self.left is None.
            if self.left is None:
                # If it is, return false.
                return False
            # Otherwise, call the function again on the node contained on the left side of the root node's tree.
            else:
                found = self.left.contains(target)

        # If the value of the node is less than the target:
        elif self.value < target:
            # Check to see if self.right is None.
            if self.right is None:
                # If it is, return false.
                return False
            # Otherwise, call the function again on the node contained on the right side of the root node's tree.
            found = self.right.contains(target)
        return found

    # We need to check nodes on the right side of the tree to find the one with the greatest value.
    def get_max(self):
        # Define current_node as self.

        # Iterative solution.
        # current = self

        # while(current.right is not None):
        #     current = current.right
        # return current.value

        # recursive solution.
        if self.right is None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        if(self.left):
            self.left.for_each(fn)
        fn(self.value)
        if(self.right):
            self.right.for_each(fn)


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

"""
What's happening in here is we're having to loop through every item in both lists to check for matches. 
That's crazy slow. What we could do instead is populate a binary search tree because that will have built-in ordering.
Then we can quickly search for duplicate values using built-in functions in the tree.
"""


# Big O -
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
THE PLAN - 
1) If there isn't a name in the tree, we need to add it.
    # Going to be a for loop to populate tree.
2) We need to check the nodes in the tree to see if there are duplicates from name_2.
    # This will be a contains call using items from name_2. Another for loop.
3) If there is a duplicate, append duplicate to duplicates list.
"""

# This is the tree we're going to create. Starting from None.
names_tree = None

# Create a loop to create the tree.
# BigO - O(n)
for name in names_1:
    if names_tree is None:
        names_tree = BSTNode(name)
    names_tree.insert(name)

# Create a loop to check values against those contained in our tree.

# BigO - I'm pretty sure this is O(log n) because we're able to take advantage of the sorting properties of the tree.
for name in names_2:
    if names_tree.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicated1 = set(names_1).intersection(names_2)
duplicated2 = set(names_1) & set(names_2)

print("duplicated names 1: ", duplicated1)
print("duplicated length 1: ", len(duplicated1))

print("duplicated names 2: ", duplicated2)
print("duplicated length 2: ", len(duplicated2))

# def has_duplicates(lst):
#     return len(lst) != len(set(lst))


# x = [1, 2, 3, 4, 4, 5, 6, 6]
# y = [1, 2, 3, 4, 5, 6]

# print("names_1 has duplicates: ", has_duplicates(names_1))
# print("names_2 has duplicates: ", has_duplicates(names_2))
