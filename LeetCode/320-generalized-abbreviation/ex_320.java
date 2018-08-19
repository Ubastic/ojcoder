public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> res = new ArrayList<>();
        helper(res, word, "", 0, true);
        return res;
    }
    
    private void helper(List<String> res, String word, String abbr, int i, boolean useNumber) {
        if (i == word.length()) {
            res.add(abbr);
            return;
        }
        helper(res, word, abbr + word.charAt(i), i + 1, true);
        if (useNumber) {
            for (int j = 1; i + j <= word.length(); j++) {
                helper(res, word, abbr + Integer.toString(j), i + j, false);
            }
        }
    }
}