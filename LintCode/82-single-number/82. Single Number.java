public class Solution {
    /**
      *@param A : an integer array
      *return : a integer 
      */
    public int singleNumber(int[] A) {
        // Write your code here
        if(A == null || A.length == 0) return 0;
        
        int ans = 0;
        
        for(int num : A) ans ^= num;
        
        return ans;
    }
}
