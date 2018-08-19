public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: the median of numbers
     */
    public int[] medianII(int[] nums) {
        // write your code here
        PriorityQueue<Integer> left = new PriorityQueue<Integer>(nums.length, Collections.reverseOrder());
        PriorityQueue<Integer> right = new PriorityQueue<Integer>();
        
        int[] ans = new int[nums.length];
        
        ans[0] = nums[0];
        left.offer(nums[0]);
        
        for(int i = 1; i < nums.length; i++){
            if(nums[i] > left.peek()){
                if(left.size() == right.size()){
                    right.offer(nums[i]);
                    left.offer(right.poll());
                }else right.offer(nums[i]);
            }else{
                if(left.size() == right.size()) left.offer(nums[i]);
                    
                else{
                    left.offer(nums[i]);
                    right.offer(left.poll());
                }
            }
            ans[i] = left.peek();
        }
        
        return ans;
    }
}
