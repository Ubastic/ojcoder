class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        rem = x
        digits = int(math.log(rem,10)) + 1

        # LSB: x % 10
        # MSB: x / (10 ** digits)
        
        msb_mask = 10 ** (digits - 1)
        for i in range(digits / 2):
            if rem % 10 != rem / msb_mask:
                return False
            rem %= msb_mask
            rem /= 10
            msb_mask /= 100
        return True
