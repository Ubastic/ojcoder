class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        middle = ['', '0', '1', '8']
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        return sum(self.count(mid, pairs, low, high) for mid in middle)
    
    def count(self, prev, pairs, low, high):
        if len(prev) > len(high) or (len(prev) == len(high) and prev > high):
            return 0
        count = 0
        if len(prev) > len(low) or (len(prev) == len(low) and prev >= low):
            if prev[0] != '0' and prev[-1] != '0' or len(prev) == 1:
                count += 1
        for i in range(5):
            count += self.count(pairs[i][0] + prev + pairs[i][1], pairs, low, high)
        return count