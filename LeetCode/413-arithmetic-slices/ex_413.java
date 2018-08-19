public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int diff = Integer.MAX_VALUE;
        int count = 0;
        int n = 0;
        for (int i = 1; i < A.length; i++) {
            if (diff != A[i] - A[i-1]) {
                diff = A[i] - A[i-1];
                count += (1 + n) * n / 2;
                n = 0;
            }
            else
                n++;
        }
        if (n > 0)
            count += (1 + n) * n / 2;
        return count;
    }
}