public class Solution {
    public int[] constructRectangle(int area) {
        int n = (int)Math.sqrt(area);
        while (area % n != 0)   --n;
        return new int[]{area / n, n};
    }
}