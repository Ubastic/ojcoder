/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        ArrayList<Interval> result = new ArrayList<Interval>();
        // write your code here
        if(intervals == null || intervals.size() == 0){
            result.add(newInterval);
            return result;
        }
        
        for(int i = 0; i < intervals.size(); i++){
            if(intervals.get(i).end < newInterval.start) result.add(intervals.get(i));
            
            else{
                if(intervals.get(i).start > newInterval.end){
                    result.add(newInterval);
                    
                    while(i < intervals.size()) result.add(intervals.get(i++));
                    
                    return result;
                }else{
                    newInterval.start = Math.min(newInterval.start, intervals.get(i).start);
                    newInterval.end = Math.max(newInterval.end, intervals.get(i).end);
                }
            }
        }
        
        if(result.isEmpty() || newInterval.start > result.get(result.size() - 1).start) result.add(newInterval);
        
        return result;
    }
}
