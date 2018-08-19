public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        if(nums == null || nums.length == 0) return 0;
        
        List<Integer> l = new ArrayList<>();
        
        for(int num : nums){
            int start = 0, end = l.size() - 1;
            
            while(start <= end){
                int mid = (start + end) / 2;
                
                if(l.get(mid) == num) break;
                
                else if(l.get(mid) > num) end = mid - 1;
                
                else start = mid + 1;
            }
            
            if(start == l.size()) l.add(num);
            
            else l.set(start, num);
        }
        
        return l.size();
    }
}
