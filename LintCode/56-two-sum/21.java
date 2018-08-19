public class Solution {
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        int[] sum = new int[2];
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                if(target - numbers[i] == numbers[j]) {
                    sum[0] = i + 1;
                    sum[1] = j + 1;
                }
            }
        }
        return sum;
    }
}
