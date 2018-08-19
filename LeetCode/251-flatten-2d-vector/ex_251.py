class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i, self.j = 0, 0
        
    def next(self):
        """
        :rtype: int
        """
        n = self.vec2d[self.i][self.j]
        self.j += 1
        return n

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.vec2d):
            while self.j < len(self.vec2d[self.i]):
                return True
            self.i += 1
            self.j = 0
        return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())