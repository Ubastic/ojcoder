class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        remain = {}
        bulls = 0
        glist = list(guess)
        for i in range(len(secret)):
            if secret[i] == glist[i]:
                bulls += 1
                glist[i] = ' '
            elif remain.has_key(secret[i]):
                remain[secret[i]] += 1
            else:
                remain[secret[i]] = 1
        cows = 0
        for c in glist:
            if remain.has_key(c) and remain[c] > 0:
                cows += 1
                remain[c] -= 1
        return str(bulls) + "A" + str(cows) + "B"