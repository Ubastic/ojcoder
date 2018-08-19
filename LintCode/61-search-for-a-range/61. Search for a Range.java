public class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        int[] ans = {-1, -1};
        
        if(A == null || A.length == 0) return ans;
        
        int start = 0, end = A.length - 1;
        
        while(start <= end){
            int mid = (start + end) / 2;
            
            if(A[mid] <= target) start = mid + 1;
            
            else end = mid - 1;
        }
        
        if(end >= 0 && A[end] == target) ans[1] = end;
        
        else return ans;
        
        start = 0;
        end = A.length - 1;
        
        while(start <= end){
            int mid = (start + end) / 2;
            
            if(A[mid] >= target) end = mid - 1;
            
            else start = mid + 1;
        }
        
        if(start < A.length && A[start] == target) ans[0] = start;
        
        return ans;
    }
}
