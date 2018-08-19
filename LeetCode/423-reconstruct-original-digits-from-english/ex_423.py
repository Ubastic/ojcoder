class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = dict()
        res = []
        mmap = [('w', 'two', 2),
                ('z', 'zero', 0),
                ('x', 'six', 6),
                ('s', 'seven', 7),
                ('v', 'five', 5),
                ('f', 'four', 4),
                ('o', 'one', 1),
                ('g', 'eight', 8),
                ('r', 'three', 3),
                ('n', 'nine', 9)]
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        for k, ns, ni in mmap:
            while k in table and table[k] > 0:
                res.append(ni)
                for c in ns:
                    table[c] -= 1
        return ''.join(map(str,sorted(res)))