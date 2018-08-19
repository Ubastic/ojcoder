public class Solution {
    /**
     * @param numbers : Give an array numbersbers of n integer
     * @param target : you need to find four elements that's sum of target
     * @return : Find all unique quadruplets in the array which gives the sum of
     *           zero.
     */
    public ArrayList<ArrayList<Integer>> fourSum(int[] numbers, int target) {
        /* your code */
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        
        if(numbers == null || numbers.length < 4) return ans;
        
        Arrays.sort(numbers);
        
        for(int i = 0; i < numbers.length - 3; i++){
            if(i > 0 && numbers[i] == numbers[i - 1]) continue;
            
            for(int j = i + 1; j < numbers.length - 2; j++){
                if(j > i + 1 && numbers[j] == numbers[j - 1]) continue;
                
                int start = j + 1, end = numbers.length - 1;
                
                while(start < end){
                    while(start > j + 1 && start < end && numbers[start] == numbers[start - 1]) start++;
                    
                    while(end < numbers.length - 1 && start < end && numbers[end] == numbers[end + 1]) end--;
                    
                    if(start == end) break;
                    
                    int sum = numbers[i] + numbers[j] + numbers[start] + numbers[end];
                    
                    if(sum == target){
                        ArrayList<Integer> l = new ArrayList<>();
                        
                        l.add(numbers[i]);
                        l.add(numbers[j]);
                        l.add(numbers[start]);
                        l.add(numbers[end]);
                        ans.add(l);
                        
                        start++;
                        end--;
                    }else if(sum < target) start++;
                    
                    else end--;
                }
            }
        }
        
        return ans;
    }
}
