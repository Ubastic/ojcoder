public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> res = new ArrayList<>();
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '+' && s.charAt(i-1) == '+') {
                StringBuilder sb = new StringBuilder();
                sb.append(s.substring(0, i-1));
                sb.append("--");
                sb.append(s.substring(i+1));
                res.add(sb.toString());
            }
        }
        return res;
    }
}