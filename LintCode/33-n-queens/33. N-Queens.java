class Solution {
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    private HashSet<Integer> locations = new HashSet<>();
     
    private ArrayList<String> copyMatrix(char[][] org){
        ArrayList<String> copy = new ArrayList<>();
        
        for(char[] str : org) copy.add(new String(str));
        
        return copy;
    }
    
    private boolean isValid(int n, int row, int col){
        for(int location : locations){
            int r = location / n, c = location % n;
            
            if(c == col || Math.abs(row - r) == Math.abs(col - c)) return false;
        }
        
        return true;
    }
    
    private void helper(char[][] matrix, ArrayList<ArrayList<String>> ans, int index){
        int n = matrix.length;
        
        if(index == n){
            ans.add(copyMatrix(matrix));
            return;
        }
        
        for(int i = 0; i < n; i++){
            if(isValid(n, index, i)){
                int location = index*n + i;
                
                locations.add(location);
                matrix[index][i] = 'Q';
                helper(matrix, ans, index + 1);
                matrix[index][i] = '.';
                locations.remove(location);
            }
        }
    }
     
    ArrayList<ArrayList<String>> solveNQueens(int n) {
        // write your code here
        ArrayList<ArrayList<String>> ans = new ArrayList<>();
        
        if(n <= 0){
            ans.add(new ArrayList<String>());
            return ans;
        }
        
        char[][] matrix = new char[n][n];
        
        for(char[] line : matrix) Arrays.fill(line, '.');
        
        helper(matrix, ans, 0);
        
        return ans;
    }
};
