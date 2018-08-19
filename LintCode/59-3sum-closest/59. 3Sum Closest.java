public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target : An integer
     * @return : return the sum of the three integers, the sum closest target.
     */
    public int threeSumClosest(int[] numbers, int target) {
        // write your code here
        Arrays.sort(numbers);
        
        int ans = numbers[0] + numbers[1] + numbers[2];
        
        for(int i = 0; i < numbers.length - 2; i++){
            if(i > 0 && numbers[i] == numbers[i - 1]) continue;
            
            int start = i + 1, end = numbers.length - 1;
            
            while(start < end){
                while(start > i + 1 && start < end && numbers[start] == numbers[start - 1]) start++;
                
                while(end < numbers.length - 1 && start < end && numbers[end] == numbers[end + 1]) end--;
                
                if(start == end) break;
                
                int sum = numbers[i] + numbers[start] + numbers[end];
                
                if(sum == target){
                    ans = sum;
                    break;
                }else if(sum < target){
                    if(Math.abs(sum - target) < Math.abs(ans - target)) ans = sum;
                    
                    start++;
                }else{
                    if(Math.abs(sum - target) < Math.abs(ans - target)) ans = sum;
                    
                    end--;
                }
            }
        }
        
        return ans;
    }
}
