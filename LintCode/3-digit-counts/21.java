class Solution {
    /*
     * param k : As description.
     * param n : As description.
     * return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        // write your code here
        long base = 1, ans = k == 0 ? 1 : 0;
        
        while(n >= base){
            long prefix = (long)n / base / 10, digit = (long)n / base % 10, suffix = (long)n % base;
            
            if(digit < k) ans += prefix*base;
                
            else if(digit == k) ans += (k == 0 ? (prefix - 1)*base : prefix*base) + 1 + suffix;
            
            else ans += k == 0 ? prefix*base : (prefix + 1)*base;
            
            base *= 10;
        }
        
        return (int) ans;
    }
};
