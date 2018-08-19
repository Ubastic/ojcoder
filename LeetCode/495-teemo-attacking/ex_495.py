class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:  return 0
        count = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i - 1] + duration <= timeSeries[i]:
                count += duration
            else:
                count += timeSeries[i] - timeSeries[i - 1]
        return count