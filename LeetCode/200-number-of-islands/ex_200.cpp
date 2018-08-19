class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int x = 0; x != grid.size(); ++x) {
            for (int y = 0; y != grid[0].size(); ++y) {
                if (grid[x][y] == '1') {
                    ++count;
                    dfs(grid, x, y);
                }
            }
        }
        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int x, int y) {
        if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] != '1')    return;
        grid[x][y] = '0';
        for (int i = 0; i < 4; i++) {
            dfs(grid, x + direction[i][0], y + direction[i][1]);
        }
    }    
    vector<vector<int>> direction = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
};