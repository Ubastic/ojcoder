class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0
        self.print_first = True

    def next(self):
        """
        :rtype: int
        """
        n  = None
        if self.hasNext():
            if self.j < len(self.v2) and self.i < len(self.v1):
                if self.print_first:
                    n = self.v1[self.i]
                    self.i += 1
                else:
                    n = self.v2[self.j]
                    self.j += 1
            elif self.j < len(self.v2):
                n = self.v2[self.j]
                self.j += 1
            else:
                n = self.v1[self.i]
                self.i += 1
        self.print_first =  False if self.print_first else True
        return n
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.v1) or self.j < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())