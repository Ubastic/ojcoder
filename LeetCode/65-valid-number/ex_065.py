class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        BLK = 0
        SIGN = 1
        DIGIT = 2
        DOT = 3
        E = 4
        
        states = [{},
                {BLK: 1, SIGN: 2, DIGIT: 3, DOT: 4},
                {DIGIT: 3, DOT: 4},
                {DIGIT: 3, DOT: 5, E: 6, BLK: 9},
                {DIGIT: 5},
                {DIGIT: 5, E: 6, BLK: 9},
                {SIGN: 7, DIGIT: 8},
                {DIGIT: 8},
                {DIGIT: 8, BLK: 9},
                {BLK: 9}]
                
        curr = 1
        for c in s:
            if '0' <= c <= '9':
                next_state = DIGIT
            elif c in '+-':
                next_state = SIGN
            elif c == '.':
                next_state = DOT
            elif c == 'e':
                next_state = E
            elif c == ' ':
                next_state = BLK
            else:
                next_state = None
            if next_state not in states[curr]:
                return False
            curr = states[curr][next_state]
        if curr not in [3, 5, 8, 9]:
            return False
        return True