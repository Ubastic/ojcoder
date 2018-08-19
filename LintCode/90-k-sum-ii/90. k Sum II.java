public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return a list of lists of integer 
     */ 
    private ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
    
    private void helper(int[] A, int k, int target, int sum, int index, List<Integer> l){
        if(k == 0){
            if(sum == target){
                ArrayList<Integer> newL = new ArrayList<>();
                
                newL.addAll(l);
                ans.add(newL);
            }
            return;
        }
        
        for(int i = index; i <= A.length - k; i++){
            l.add(A[i]);
            helper(A, k - 1, target, sum + A[i], i + 1, l);
            l.remove(l.size() - 1);
        }
    }
     
    public ArrayList<ArrayList<Integer>> kSumII(int[] A, int k, int target) {
        // write your code here
        if(A == null || A.length == 0) return ans;
        
        helper(A, k, target, 0, 0, new ArrayList<Integer>());
        
        return ans;
    }
}
