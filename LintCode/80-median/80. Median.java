public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    private void swap(int[] nums, int x, int y){
        int tmp = nums[x];
        nums[x] = nums[y];
        nums[y] = tmp;
    } 
     
    public int median(int[] nums) {
        // write your code here
        int start = 0, end = nums.length - 1, medianIndex = (nums.length - 1) / 2;
        
        while(true){
            int lo = start, hi = end + 1;
            
            while(true){
                while(lo < end && nums[++lo] < nums[start]);
                
                while(start < hi && nums[--hi] > nums[start]);
                
                if(lo >= hi) break;
                
                swap(nums, lo, hi);
            }
            
            swap(nums, start, hi);
            
            if(hi == medianIndex) return nums[hi];
            
            else if(hi > medianIndex) end = hi - 1;
            
            else start = hi + 1;
        }
    }
}
