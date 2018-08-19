from collections import deque

class Hit(object):
    
    def __init__(self, timestamp, count=1):
        self.timestamp = timestamp
        self.count = count

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.range_count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if self.q and self.q[-1].timestamp == timestamp:
            self.q[-1].count += 1
        else:
            hit = Hit(timestamp)
            self.q.append(hit)
        self.range_count += 1
        self._update(timestamp)
        
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self._update(timestamp)
        return self.range_count
        
    def _update(self, timestamp):
        while self.q and timestamp - self.q[0].timestamp >= 300:
            self.range_count -= self.q[0].count
            self.q.popleft()


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)