class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator: return 'NaN'
        is_negative = False
        if numerator < 0:   
            numerator = -numerator
            is_negative = not is_negative
        if denominator < 0: 
            denominator = -denominator
            is_negative = not is_negative
        dec = '0'
        fraction = ''
        seen = {}
        if numerator >= denominator:
            dec = str(numerator / denominator)
            numerator = numerator % denominator
        while numerator:
            if numerator in seen:
                fraction = fraction[:seen[numerator]] + '(' + fraction[seen[numerator]:] + ')'
                break
            seen[numerator] = len(fraction)
            fraction += str(numerator * 10 / denominator)
            numerator = numerator * 10 % denominator
        res = dec
        if fraction:    res += '.' + fraction
        return '-' + res if is_negative and res != '0' else res 