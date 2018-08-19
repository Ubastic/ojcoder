public class Solution {
	/** 
     *@param nums: The integer array you should partition
     *@param k: As description
     *return: The index after partition
     */
    private void swap(int[] nums, int x, int y){
        int tmp = nums[x];
        nums[x] = nums[y];
        nums[y] = tmp;
    }
    
    public int partitionArray(int[] nums, int k) {
	    //write your code here
	    if(nums == null || nums.length == 0) return 0;
	    
	    int start = 0, end = nums.length - 1;
	    
	    while(true){
	        while(start < end && nums[start] < k) start++;
	        
	        while(start < end && nums[end] >= k) end--;
	        
	        if(start >= end) break;
	        
	        swap(nums, start, end);
	    }
	    
	    return nums[end] < k ? end + 1 : end;
    }
}
