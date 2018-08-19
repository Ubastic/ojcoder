from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myset = set()
        self.lst = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            self.lst.append(val)
            return False
        else:
            self.myset.add(val)
            self.lst.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            self.myset.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.myset):
            n = len(self.lst)
            idx = randint(0, n-1)
            while self.lst[idx] not in self.myset:
                idx = randint(0, n-1)
            return self.lst[idx]
        else:
            return None
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()