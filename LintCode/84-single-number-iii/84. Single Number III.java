public class Solution {
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    public List<Integer> singleNumberIII(int[] A) {
        // write your code here
        List<Integer> ans = new ArrayList<Integer>();
        
        if(A == null || A.length == 0) return ans;
        
        int oneIndex = 0;
        int aXORb = 0;
        
        for(int num : A) aXORb ^= num;

        while(aXORb != 0){
            if((aXORb & 1) == 1) break;
            
            oneIndex++;
            aXORb >>= 1;
        }
        
        int a = 0, b = 0;
        
        for(int num : A){
            if(((num >> oneIndex) & 1) == 1) a ^= num;
            
            else b ^= num;
        }
            
        ans.add(a);
        ans.add(b);
        
        return ans;
    }
}
