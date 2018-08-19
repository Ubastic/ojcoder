public class Solution {
    /**
     * @param nums: A list of integers
     * @return: The majority number that occurs more than 1/3
     */
    private boolean check(ArrayList<Integer> nums, int checkNum){
        int count = 0;
        
        for(int num : nums)
            if(num == checkNum) count++;
        
        return count > nums.size() / 3 ? true : false;
    }
    
    public int majorityNumber(ArrayList<Integer> nums) {
        // write your code
        int count = 0, major = 0, n = nums.size();
        
        for(int i = 0; i < 2*n/3; i++){
            if(count == 0) major = nums.get(i);
            
            if(major == nums.get(i)) count++;
            
            else count--;
        }
        
        if(check(nums, major)) return major;
            
        count = 0;
        
        for(int i = n / 3; i < n; i++){
            if(count == 0) major = nums.get(i);
            
            if(major == nums.get(i)) count++;
            
            else count--;
        }
        
        if(check(nums, major)) return major;
            
        count = 0;
        
        for(int i = 0; i < n; i++){
            if(i == n / 3) i = n*2 / 3 - 2;
            
            if(count == 0) major = nums.get(i);
            
            if(major == nums.get(i)) count++;
            
            else count--;
        }
        
        return major;
    }
}
