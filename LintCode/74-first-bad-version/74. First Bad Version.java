/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        long start = 1, end = n;
        
        while(start <= end){
            long mid = (start + end) / 2;
            
            if(SVNRepo.isBadVersion((int)mid)) end = mid - 1;
            
            else start = mid + 1;
        }
        
        return (int)start;
    }
}
