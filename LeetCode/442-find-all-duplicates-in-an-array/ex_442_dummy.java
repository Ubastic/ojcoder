public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        HashSet<Integer> hSet = new HashSet<>();
        for (int n : nums) {
            if (hSet.contains(n))
                res.add(n);
            else
                hSet.add(n);
        }
        return res;
    }
}