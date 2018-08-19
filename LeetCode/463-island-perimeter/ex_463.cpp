class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int count = 0;
        for (int x = 0; x != grid.size(); ++x) {
            for (int y = 0; y != grid[0].size(); ++y) {
                count += grid[x][y] * 4;
                if (grid[x][y] == 1)
                    count -= adjacent(grid, x, y);
            }
        }
        return count;
    }
private:
    int offset[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int adjacent(vector<vector<int>>& grid, int x, int y) {
        int count = 0;
        for (int i = 0; i != 4; ++i) {
            int nx = offset[i][0] + x;
            int ny = offset[i][1] + y;
            if (0 <= nx && nx < grid.size() && 0 <= ny && ny < grid[0].size() && grid[nx][ny] == 1)
                ++count;
        }
        return count;
    }
};