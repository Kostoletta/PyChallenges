import collections
import random


class Store:
    """
    Code Written as an Exercise

    Features:
        Create a class that allows storing values allowing duplicates.
        It allows inserting values, deleting a given value, and retrieving a random value in constant time O(1).
    """

    def __init__(self):
        self.values = []
        self.indexes = collections.defaultdict(set)

    def add(self, value):
        self.values.append(value)
        self.indexes[value].add(len(self.values) - 1)

    def delete(self, value):
        if value not in self.indexes:
            return
        last_value = self.values[-1]
        print(f"Value {value}")
        print(f"last val {last_value}")

        if value != last_value:
            index = next(iter(self.indexes[value]))
            self.values[index] = last_value
            self.indexes[value].remove(index)
            self.indexes[last_value].add(index)

        self.indexes[last_value].remove(len(self.values) - 1)
        self.values.pop()
        if len(self.indexes[value]) == 0:
            del self.indexes[value]

    def get_random(self):
        return random.choice(self.values) if self.values else None

    def get_status(self):
        """
        Prints the current state of the class, used to debug and to visualize the current state
        """
        print(self.values)
        print(self.indexes)
        print()
