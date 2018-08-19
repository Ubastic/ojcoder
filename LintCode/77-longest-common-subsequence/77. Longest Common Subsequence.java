public class Solution {
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    public int longestCommonSubsequence(String A, String B) {
        // write your code here
        if(A == null || A.length() == 0 || B == null || B.length() == 0) return 0;
        
        char[] charA = A.toCharArray(), charB = B.toCharArray();
        int[][] DP = new int[A.length() + 1][B.length() + 1];
        int maxSteps = 0;
        
        for(int i = 1; i <= charA.length; i++)
            for(int j = 1; j <= charB.length; j++){
                if(charA[i - 1] == charB[j - 1]) DP[i][j] = DP[i - 1][j - 1] + 1;
                
                else DP[i][j] = Math.max(DP[i - 1][j], DP[i][j - 1]);
                
                maxSteps = Math.max(maxSteps, DP[i][j]);
            }
        
        return maxSteps;
    }
}
