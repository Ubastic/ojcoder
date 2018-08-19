public class Solution {
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        HashMap<Integer, HashSet<Integer>> numToIndexes = new HashMap<>();
        
        for(int i = 0; i < numbers.length; i++){
            int diff = target - numbers[i];
            
            if(numToIndexes.containsKey(diff)) 
                numToIndexes.get(diff).add(i);
            else{
                HashSet<Integer> set = new HashSet<>();
                set.add(i);
                numToIndexes.put(diff, set);
            }
        }
        
        int[] ans = new int[2];
        
        for(int i = 0; i < numbers.length; i++){
            if(numToIndexes.containsKey(numbers[i])){
                int index = numToIndexes.get(numbers[i]).iterator().next();
                
                if(index != i){
                    ans[0] = Math.min(i, index) + 1;
                    ans[1] = Math.max(i, index) + 1;
                    break;
                }
            }
        }
        
        return ans;
    }
}
