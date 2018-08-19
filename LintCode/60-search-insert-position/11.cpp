class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
public:
    int searchInsert(vector<int> &A, int target) {
        // write your code here
        int lo = 0;
        int hi = A.size()-1;
        while(lo<=hi){
            int mid = lo + (hi - lo)/2;
            if(A[mid] == target){
                return mid;
            }
            if(target > A[mid]){
                lo = mid + 1;
            }else{
                hi = mid - 1;
            }
        }
        return lo;
    }
};
