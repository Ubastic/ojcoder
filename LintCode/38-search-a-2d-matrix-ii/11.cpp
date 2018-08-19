class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        int cnt = 0;
        int m = matrix.size();
        if(m == 0)
            return cnt;
        int n = matrix[0].size();
        if(n == 0)
            return cnt;
            
        int i = 0;
        int j = n-1;
        
        while(i < m && j >= 0){
            if(target > matrix[i][j]){
                i++;
            }else{
                if(target == matrix[i][j])
                    cnt++;
                j--;
            }
        }
        return cnt;
    }
};
