/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: C++
*/

class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &array, int target) {
        // write your code here
        int lo = 0;
        int hi = array.size()-1;
        
        while(lo<=hi){
            int mid = lo + (hi - lo)/2;
            if(array[mid] == target){
                if(lo == hi)
                    return lo;
                hi = mid;
                continue;
            }
            if(array[mid] > target){
                hi = mid -1;
                continue;
            }
            if(array[mid] < target){
                lo = mid +1;
                continue;
            }
        }
        
        return -1;
    }
};
