public class Solution {
    public int islandPerimeter(int[][] grid) {
        int count = 0;
        for (int x = 0; x != grid.length; ++x) {
            for (int y = 0; y != grid[0].length; ++y) {
                count += grid[x][y] * 4;
                if (grid[x][y] == 1)
                    count -= adjacent(grid, x, y);
            }
        }
        return count;
    }
    
    private static final int[][] offset = new int[][] { {0, 1}, {1, 0}, {-1, 0}, {0, -1} };

    private int adjacent(int[][] grid, int x, int y) {
        int count = 0;
        for (int i = 0; i < 4; i++) {
            int nx = offset[i][0] + x;
            int ny = offset[i][1] + y;
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] == 1)
                ++count;
        }
        return count;
    }
}