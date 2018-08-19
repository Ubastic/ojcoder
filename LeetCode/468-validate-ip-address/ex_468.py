class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        i = 0
        output = ['Neither', 'IPv4', 'IPv6']
        if '.' in IP:   # ipv4
            nums = IP.split('.')
            if len(nums) != 4:  return output[i]
            for n in nums:
                if len(n) > 3 or len(n) == 0 or (n[0] == '0' and len(n) != 1) or not n.isdigit() or int(n) > 255:    return output[i]
            i = 1
        else:           # ipv6
            nums = IP.lower().split(':')
            if len(nums) < 3 or len(nums) > 8:  return output[i]
            for n in nums:
                if len(n) > 4 or len(n) == 0: 
                    return output[i]
                for c in n:
                    if c not in '0123456789abcdef': 
                        return output[i]
            i = 2
        return output[i]