public class Solution {
    /**
     * @param A: An integer array.
     * @param target: An integer.
     */
    public int MinAdjustmentCost(ArrayList<Integer> A, int target) {
        // write your code here
        int n = A.size();  
        if (n < 2) {  
            return 0;  
        }  
        // init  
        int[][] cost = new int[n][100];  
        for (int i = 0; i < 100; i++) {  
            cost[0][i] = Math.abs(A.get(0) - (i + 1)); //A[0]到i + 1的距离  
        }  
          
        for (int i = 1; i < n; i++) {  
            for (int j = 0; j < 100; j++) {  
                int diff = Math.abs(A.get(i) - (j + 1)); //A[i]到j + 1的距离  
                int upper = Math.min(j + target, 99); //k的上界  
                int lower = Math.max(j - target, 0); //k的下界  
                cost[i][j] = Integer.MAX_VALUE;  
                for (int k = lower; k <= upper; k++) {  
                    cost[i][j] = Math.min(cost[i][j], cost[i-1][k] + diff);  
                } // for  
            } // for  
        } // for  
        // 最优解  
        int min = Integer.MAX_VALUE;  
        for (int i = 0; i < 100; i++) {  
            min = Math.min(min, cost[n - 1][i]);  
        }  
        return min;  
    }
}
