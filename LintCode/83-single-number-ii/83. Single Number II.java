public class Solution {
	/**
	 * @param A : An integer array
	 * @return : An integer 
	 */
    public int singleNumberII(int[] A) {
        // write your code here
        if(A == null || A.length == 0) return 0;
        
        int[] bits = new int[32];
        
        for(int num : A)
            for(int i = 31; i >= 0; i--){
                bits[i] += num & 1;
                num >>= 1;
            }
        
        int ans = 0;
        
        for(int i = 0; i < 32; i++) ans = (ans << 1) | bits[i] % 3;
        
        return ans; 
    }
}
