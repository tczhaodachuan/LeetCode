import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.set = dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.set.has_key(val):
            return False
        self.nums.append(val)
        self.set[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.set.has_key(val):
            return False

        index = self.set[val]
        last_key = self.nums[len(self.nums) - 1]
        self.nums[index] = last_key
        # update last_key's index to the one which got removed
        self.set[last_key] = index
        # throw away the last element in nums
        self.nums.pop()
        self.set.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


class RandomizedSetII(object):
    def __init__(self):
        self.keys = []
        self.dictionary = dict()

    def insert(self, val):
        if val == None:
            return False
        if self.dictionary.has_key(val):
            self.keys.append(val)
            # append the value's index into the dictionary
            self.dictionary[val].add(len(self.keys) - 1)
            return False
        self.keys.append(val)
        indexSet = set()
        indexSet.add(len(self.keys) - 1)
        self.dictionary[val] = indexSet
        return True

    def remove(self, val):
        if not self.dictionary.has_key(val):
            return False

        # pop out the last key
        last_key_index = len(self.keys) - 1
        last_key = self.keys.pop()
        if last_key == val:
            # pop out the last index which matches the val
            self.dictionary[val].remove(last_key_index)

        if last_key != val:
            # pop out the last index which matches the val
            index = self.dictionary[val].pop()
            # remove last_key_index in the dictionary
            self.dictionary[last_key].remove(last_key_index)
            # change it to the new index which is going to be removed
            self.dictionary[last_key].add(index)
            # replace the index of keys to last_key
            self.keys[index] = last_key

        if len(self.dictionary[val]) == 0:
            # if the dictionary of val has no index, delete it
            self.dictionary.pop(val)
        return True

    def getRandom(self):
        return self.keys[random.randint(0, len(self.keys) - 1)]


if __name__ == '__main__':
    randomSet = RandomizedSet()
    print randomSet.insert(2)
    print randomSet.insert(6)
    print randomSet.remove(2)
    print randomSet.getRandom()

    randomSetII = RandomizedSetII()
    print randomSetII.insert(None)
    print randomSetII.insert(4)
    print randomSetII.insert(3)
    print randomSetII.insert(4)
    print randomSetII.insert(2)
    print randomSetII.insert(2)

    print randomSetII.dictionary
    print randomSetII.keys
    print randomSetII.remove(2)
    print randomSetII.remove(2)
    print randomSetII.remove(2)
    print randomSetII.dictionary
    print randomSetII.keys
