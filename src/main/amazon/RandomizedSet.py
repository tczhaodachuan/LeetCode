class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.values_dict = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.values_dict:
            return False
        self.values.append(val)
        self.values_dict[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.values_dict:
            return False

        index = self.values_dict[val]
        last_val_index = len(self.values) - 1
        last_val = self.values[last_val_index]
        if index == last_val_index:
            self.values.pop(-1)
            self.values_dict.pop(val)
            return True

        self.values[index] = last_val
        self.values_dict[last_val] = index
        self.values.pop(-1)
        self.values_dict.pop(val)
        return True



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.values) == 0:
            raise ValueError("The set contains no elements")
        import random
        return self.values[random.randint(0, len(self.values) - 1)]