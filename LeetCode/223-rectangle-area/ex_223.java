public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int interaction = 0;
        int r1 = (C - A) * (D - B);
        int r2 = (G - E) * (H - F);
        
        if (C > E && G > A && D > F && H > B)
            interaction = (Math.min(C, G) - Math.max(A, E)) * (Math.min(D, H) - Math.max(B, F));
        
        return r1 + r2 - interaction;
    }
}