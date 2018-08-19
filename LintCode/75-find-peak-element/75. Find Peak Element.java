class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        int start = 1, end = A.length - 2;
        
        while(start < end){
            int mid = (start + end) / 2;
            
            if(A[mid] <= A[mid - 1]) end = mid - 1;
            
            else if(A[mid] <= A[mid + 1]) start = mid + 1;
            
            else return mid;
        }
        
        return start;
    }
}
