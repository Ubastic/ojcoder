/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> counter = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        int modeCount = getModeCount(root, counter);
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            int key = entry.getKey();
            int value = entry.getValue();
            if (value == modeCount) res.add(key);
        }
        int[] resArray = new int[res.size()];
        for(int i = 0; i < resArray.length; i++) resArray[i] = res.get(i);
        return resArray;
    }
    private int getModeCount(TreeNode root, Map<Integer, Integer> counter) {
        if (root == null)   return 0;
        counter.put(root.val, counter.getOrDefault(root.val, 0) + 1);
        return Math.max(counter.get(root.val), Math.max(getModeCount(root.left, counter), getModeCount(root.right, counter)));
    }
}