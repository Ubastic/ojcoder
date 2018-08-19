/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 */
class Solution {
public:
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: new interval.
     * @return: A new interval list.
     */
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        // write your code here
        vector<Interval> res;
        bool merged = false;
        for(Interval it : intervals){
            if(newInterval.start <= it.end && newInterval.end >= it.start){
                newInterval.start = min(newInterval.start, it.start);
                newInterval.end = max(newInterval.end, it.end);
            }else{
                if(!merged && newInterval.end < it.start){
                    res.push_back(newInterval);
                    merged = true;
                }
                res.push_back(it);
            }
        }
        if(!merged)
            res.push_back(newInterval);
        return res;
    }
};
