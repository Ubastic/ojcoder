public class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        // write your code here
        if(A == null || A.length == 0) return 0;
        
        int start = 0, end = A.length;
        
        while(start < end){
            int mid = (start + end) / 2;
            
            if(A[mid] == target) return mid;
            
            else if(A[mid] > target) end = mid - 1;
            
            else start = mid + 1;
        }
        
        return start;
    }
}
