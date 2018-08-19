public class Solution {
    public int[] findPermutation(String s) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i <= s.length(); i++) 
            if (i == s.length() || s.charAt(i) == 'I')
                for (int j = i + 1, length = res.size(); j > length; j--)
                    res.add(j);
        int[] resArray = new int[res.size()];
        for (int i = 0; i < res.size(); i++) 
            resArray[i] = res.get(i);
        return resArray;
    }
}