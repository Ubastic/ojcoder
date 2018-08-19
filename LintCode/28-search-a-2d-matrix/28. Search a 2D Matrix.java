public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        
        int start = 0, end = matrix.length - 1;
        
        while(start < end){
            int mid = (start + end) / 2;
            
            if(matrix[mid][0] < target) start = mid + 1;
            
            else if(matrix[mid][0] > target) end = mid;
            
            else return true;
        }
        
        if(end == 0) return false;
        
        if(target < matrix[end][0]) return Arrays.binarySearch(matrix[end - 1], target) >= 0;
        
        else return Arrays.binarySearch(matrix[end], target) >= 0;
    }
}
