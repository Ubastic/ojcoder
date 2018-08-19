class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (timeSeries.size() == 0) return 0;
        int count = duration;
        for (int i = 1; i < timeSeries.size(); ++i) {
            if (timeSeries[i - 1] + duration <= timeSeries[i])
                count += duration;
            else
                count += timeSeries[i] - timeSeries[i - 1];
        }
        return count;
    }
};