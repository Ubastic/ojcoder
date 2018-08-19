class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
public:
    vector<int> searchRange(vector<int> &A, int target) {
        // write your code here
        int sz = A.size();
        int lo = 0;
        int hi = sz - 1;
        vector<int> res(2, -1);
        
        while(lo <= hi){
            int mid = lo + (hi - lo)/2;
            if(A[mid] >= target){
                hi = mid - 1;
            }else{
                lo = mid + 1;
            }
        }
        if(lo == sz || A[lo]!=target)
            return res;
        
        res[0] = lo;
        lo = 0;
        hi = sz - 1;
        while(lo <= hi){
            int mid = lo + (hi - lo)/2;
            if(A[mid] <= target){
                lo = mid + 1;
            }else{
                hi = mid - 1;
            }
        }
        res[1] = hi;
        return res;
    }
};
