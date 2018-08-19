public class Solution {
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public ArrayList<Long> productExcludeItself(ArrayList<Integer> A) {
        // write your code
        long[] left = new long[A.size()], right = new long[A.size()];
        
        left[0] = 1;
        right[A.size() - 1] = 1;
        
        for(int i = 1; i < left.length; i++) left[i] = left[i - 1]*(long)A.get(i - 1);
        
        for(int i = left.length - 2; i >= 0; i--) right[i] = right[i + 1]*(long)A.get(i + 1);
        
        ArrayList<Long> ans = new ArrayList<>();
        
        for(int i = 0; i < left.length; i++) ans.add(left[i]*right[i]);
        
        return ans;
    }
}
