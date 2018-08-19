class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.nums:
            self.nums[n] -= 1
            if value - n in self.nums and self.nums[value - n] > 0:
                return True
            self.nums[n] += 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)