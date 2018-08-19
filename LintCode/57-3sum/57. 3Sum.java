public class Solution {
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    public ArrayList<ArrayList<Integer>> threeSum(int[] numbers) {
        // write your code here
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        
        if(numbers == null || numbers.length < 3) return ans;
        
        Arrays.sort(numbers);
        
        for(int i = 0; i < numbers.length - 2; i++){
            if(i > 0 && numbers[i] == numbers[i - 1]) continue;
            
            int start = i + 1, end = numbers.length - 1;
            
            while(start < end){
                while(start > i + 1 && start < end && numbers[start] == numbers[start] - 1) start++;
                
                while(end < numbers.length - 1 && end > start && numbers[end] == numbers[end + 1]) end--;
                
                if(start == end) break;
                
                int sum = numbers[start] + numbers[end];
                
                if(sum + numbers[i] == 0){
                    ArrayList<Integer> l = new ArrayList<>();
                    l.add(numbers[i]);
                    l.add(numbers[start]);
                    l.add(numbers[end]);
                    ans.add(l);
                    start++;
                    end--;
                }else if(sum + numbers[i] > 0)
                    end--;
                else start++;
            }
        }
        
        return ans;
    }
}
