class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        int and = (a & b), xor = (a ^ b);
        
        while(and != 0){
            and <<= 1;
            int tmp = xor;
            xor = (and ^ xor);
            and = (and & tmp);
        }
        
        return xor;
    }
};
