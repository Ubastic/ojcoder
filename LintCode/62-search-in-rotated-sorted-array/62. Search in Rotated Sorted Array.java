public class Solution {
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        if(A == null || A.length == 0) return -1;
        
        int start = 0, end = A.length - 1;
        
        while(start < end){
            int mid = (start + end) / 2;
            
            if(A[mid] == target) return mid;
            
            else if(A[mid] > target){
                if(A[start] == target) return start;
                
                else if(A[start] < target) end = mid - 1;
                    
                else if(A[start] > A[mid]) end = mid - 1;
                
                else start = mid + 1;
            }else{
                if(A[end] == target) return end;
                
                else if(A[end] > target) start = mid + 1;
                
                else if(A[end] < A[mid]) start = mid + 1;
                
                else end = mid - 1;
            }
        }
        
        return A[start] == target ? start : -1;
    }
}
