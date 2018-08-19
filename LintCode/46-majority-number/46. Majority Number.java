public class Solution {
    /**
     * @param nums: a list of integers
     * @return: find a  majority number
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        // write your code
        int count = 1, ans = nums.get(0);
        
        for(int i = 1; i < nums.size(); i++){
            if(count == 0){
                ans = nums.get(i);
                count++;
            }else if(ans == nums.get(i)) count++;
                
            else count--;
        }
        
        return ans;
    }
}
