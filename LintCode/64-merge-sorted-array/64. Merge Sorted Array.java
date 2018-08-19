class Solution {
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here
        int indexA = 0, indexB = 0, indexC = 0;
        int[] C = new int[A.length];
        
        while(indexA < m && indexB < n){
            if(A[indexA] <= B[indexB]) C[indexC++] = A[indexA++];
            
            else C[indexC++] = B[indexB++];
        }
        
        while(indexA < m) C[indexC++] = A[indexA++];
        
        while(indexB < n) C[indexC++] = B[indexB++];
        
        System.arraycopy(C, 0, A, 0, C.length);
    }
}
