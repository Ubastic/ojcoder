public class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        HashMap<Integer, Integer> sumMap = new HashMap<>();
        int count = 0;
        
        for (int i : A) {
            for (int j : B) {
                sumMap.put(i + j, sumMap.getOrDefault(i + j, 0) + 1);
            }
        }
        
        for (int i : C) {
            for (int j : D) {
                if (sumMap.containsKey(-i - j)) {
                    count += sumMap.get(-i - j);
                }
            }
        }
        
        return count;
    }
}