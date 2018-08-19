/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
struct less_than_key {
    inline bool operator()(const Interval &lhs, const Interval &rhs) {
        return (lhs.start < rhs.start);
    } 
};
 
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), less_than_key());
        int i = 1;
        while (i < intervals.size()) {
            if (intervals[i].start < intervals[i-1].end)    return false;
            ++i;
        }
        return true;
    }
};