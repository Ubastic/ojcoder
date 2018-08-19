public class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<String>();
        for (int i = 1; i < n + 1; i++) {
            StringBuilder sb = new StringBuilder();
            if (i % 3 == 0)         sb.append("Fizz");
            if (i % 5 == 0)         sb.append("Buzz");
            if (sb.length() == 0)     sb.append(Integer.toString(i));
            ans.add(sb.toString());
        }
        return ans;
    }
}