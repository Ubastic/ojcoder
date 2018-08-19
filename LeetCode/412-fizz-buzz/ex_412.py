class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in xrange(1, n + 1):
            s = ''
            if i % 3 == 0:  s += 'Fizz'
            if i % 5 == 0:  s += 'Buzz'
            if not s:       s = str(i)
            ans.append(s)
        return ans