public class Solution {
    public int magicalString(int n) {
        List<Integer> s = new ArrayList<>();
        s.add(1);
        s.add(2);
        s.add(2);
        int i = 2;
        while (s.size() < n) {
            int nextNumber = 3 - s.get(s.size() - 1);
            for (int c = 0; c < s.get(i); c++)  s.add(nextNumber);
            i++;
        }
        while (s.size() > n) s.remove(s.size() - 1);
        return Collections.frequency(s, 1);
    }
}