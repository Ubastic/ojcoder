public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here
        if(A == null || A.length() == 0 || B == null || B.length() == 0) return 0;
        
        char[] charA = A.toCharArray(), charB = B.toCharArray();
        int[][] DP = new int[charA.length + 1][charB.length + 1];
        int maxLen = 0;
        
        for(int i = 1; i <= charA.length; i++)
            for(int j = 1; j <= charB.length; j++){
                if(charA[i - 1] == charB[j - 1]) DP[i][j] = DP[i - 1][j - 1] + 1;
                
                maxLen = Math.max(maxLen, DP[i][j]);
            }
        
        return maxLen;
    }
}
