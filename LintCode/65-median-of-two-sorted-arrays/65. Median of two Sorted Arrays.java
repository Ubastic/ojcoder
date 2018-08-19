class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        // write your code here
        int indexA = 0, indexB = 0, k = (A.length + B.length) / 2;
        
        while(indexA < A.length && indexB < B.length && k > 1){
            int half = k / 2;
            
            int tmpA = indexA + half - 1 < A.length ? A[indexA + half - 1] : Integer.MAX_VALUE;
            int tmpB = indexB + half - 1 < B.length ? B[indexB + half - 1] : Integer.MAX_VALUE;
            
            if(tmpA > tmpB) indexB += half;
            
            else indexA += half;
            
            k -= half;
        }
        
        if(indexA == A.length) return (A.length + B.length) % 2 == 1 ? B[indexB + k] : (B[indexB + k] + B[indexB + k - 1]) / 2d;
        
        if(indexB == B.length) return (A.length + B.length) % 2 == 1 ? A[indexA + k] : (A[indexA + k] + A[indexA + k - 1]) / 2d;
        
        int mid1 = A[indexA] <= B[indexB] ? A[indexA++] : B[indexB++], mid2 = Math.min(indexA < A.length ? A[indexA] : Integer.MAX_VALUE, indexB < B.length ? B[indexB] : Integer.MAX_VALUE);
        
        return (A.length + B.length) % 2 == 1 ? mid2 : (mid1 + mid2) / 2d;
    }
}
