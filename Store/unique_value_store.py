import collections
import random


class Store:
    """
    Code Written as an Exercise

    Features:
        Create a class that allows storing values without allowing duplicates.
        It allows inserting values, deleting a given value, and retrieving a random value in constant time O(1).
    """

    def __init__(self):
        self.values = []
        self.indexes = {}

    def add(self, value):
        if value in self.indexes:
            return
        # not present
        self.values.append(value)
        self.indexes[value] = len(self.values) - 1

    def delete(self, value):
        if value not in self.indexes:
            return
        index = self.indexes[value]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.indexes[last_val] = index
        self.values.pop()
        del self.indexes[value]

    def get_random(self):
        return random.choice(self.values)

    def get_status(self):
        """
        Prints the current state of the class, used to debug and to visualize the current state
        """
        print(self.values)
        print(self.indexes)
        print()


my_store = Store()
