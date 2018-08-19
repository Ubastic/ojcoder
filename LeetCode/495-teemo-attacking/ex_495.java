public class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.length == 0) return 0;
        int count = duration;
        for (int i = 1; i < timeSeries.length; i++) {
            if (timeSeries[i - 1] + duration <= timeSeries[i])
                count += duration;
            else
                count += timeSeries[i] - timeSeries[i - 1];
        }
        return count;
    }
}