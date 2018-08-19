class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            length = self.getLength(data[i])
            if not length:  return False
            if i + length > len(data):  return False
            for j in range(1, length):
                if data[i + j] >> 6 != 2: 
                    return False
            i += length
        return True
        
    def getLength(self, data):
        n = 0
        if data >> 7 == 0:       # 1
            n = 1
        elif data >> 5 == 6:     # 2
            n = 2
        elif data >> 4 == 14:   # 3
            n = 3
        elif data >> 3 == 30:   # 4
            n = 4
        return n