public class Solution {  
    public int[] twoSum(int[] nums, int target) {  
        Map<Integer, Integer> map = new HashMap<>();  
        for(int i=0; i<nums.length; i++) {  
            Integer pos = map.get(target-nums[i]);  
            if (pos != null) {  
                int[] pair = new int[2];  
                pair[0] = pos;  
                pair[1] = i;  
                return pair;  
            }  
            map.put(nums[i], i);  
        }  
        return null;  
    }  
}  
