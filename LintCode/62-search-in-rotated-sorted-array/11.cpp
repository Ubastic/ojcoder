class Solution {
    /** 
     * param A : an integer ratated sorted array
     * param target :  an integer to be searched
     * return : an integer
     */
public:
    int search(vector<int> &A, int target) {
        // write your code here
        int lo = 0;
        int hi = A.size()-1;
        
        while(lo<=hi){
            int mid = lo + (hi - lo)/2;
            if(A[mid] == target)
                return mid;
            if(A[mid] > A[lo]){
                if(A[lo]<=target && target<A[mid]){
                    hi = mid - 1;
                }else{
                    lo = mid + 1;
                }
            }else{
                if(A[mid]<target && target<=A[hi]){
                    lo = mid + 1;
                }else{
                    hi = mid - 1;
                }
            }
        }
        return -1;
    }
};
