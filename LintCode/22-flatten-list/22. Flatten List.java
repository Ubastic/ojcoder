/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer,
 *     // rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds,
 *     // if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds,
 *     // if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {

    // @param nestedList a list of NestedInteger
    // @return a list of integer
    private void helper(NestedInteger nl, List<Integer> resSet){
        if(nl.isInteger()) resSet.add(nl.getInteger());
        
        else for(NestedInteger n : nl.getList()) helper(n, resSet);
    }
    
    public List<Integer> flatten(List<NestedInteger> nestedList) {
        // Write your code here
        List<Integer> ans = new ArrayList<>();
        
        for(NestedInteger n : nestedList) helper(n, ans);
        
        return ans;
    }
}
