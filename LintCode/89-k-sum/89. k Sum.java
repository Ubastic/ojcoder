public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return an integer
     */
    public int kSum(int A[], int k, int target) {
        // write your code here
        if(A == null || A.length == 0) return 0;
        
        int[][][] DP = new int[A.length + 1][k + 1][target + 1];
        
        DP[0][0][0] = 1;
        
        for(int i = 1; i <= A.length; i++){
            DP[i][0][0] = 1;
            
            for(int j = 1; j <= k; j++)
                for(int t = 1; t <= target; t++)
                    DP[i][j][t] = DP[i - 1][j][t] + (t >= A[i - 1] ? DP[i - 1][j - 1][t - A[i - 1]] : 0);
        }
        
        return DP[A.length][k][target];
    }
}
