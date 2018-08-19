public class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: void
     */
    private void swap(ArrayList<Integer> nums, int x, int y){
        int tmp = nums.get(x);
        nums.set(x, nums.get(y));
        nums.set(y, tmp);
    } 
     
    public void recoverRotatedSortedArray(ArrayList<Integer> nums) {
        // write your code
        if(nums == null || nums.size() <= 1) return;
        
        int start = 0, end = nums.size() - 1;
        
        while(start < end){
            int index = start;
            
            while(index < end && nums.get(index) <= nums.get(index + 1)) index++;
            
            if(index++ == end) return;
        
            while(index <= end) swap(nums, start++, index++);
        }
    }
}
