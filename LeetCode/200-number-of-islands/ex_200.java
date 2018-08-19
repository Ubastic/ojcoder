public class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int x = 0; x < grid.length; x++) {
            for (int y = 0; y < grid[0].length; y++) {
                if (grid[x][y] == '1') {
                    count++;
                    dfs(grid, x, y);
                }
            }
        }
        return count;
    }
    
    private void dfs(char[][] grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] != '1')    return;
        grid[x][y] = '0';
        for (int i = 0; i < 4; i++) {
            dfs(grid, x + direction[i][0], y + direction[i][1]);
        }
    }
    
    private static final int[][] direction = new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
}