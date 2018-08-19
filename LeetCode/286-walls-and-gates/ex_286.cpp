class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        for (int row = 0; row != rooms.size(); ++row) {
            for (int col = 0; col != rooms[0].size(); ++col) {
                if (rooms[row][col] == 0)
                    dfs(rooms, row, col, 0);
            }
        }
    }
private:
    vector<pair<int, int>> offset{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    void dfs(vector<vector<int>>& rooms, int row, int col, int distance) {
        rooms[row][col] = min(distance, rooms[row][col]);
        for (auto& p : offset) {
            int next_row = row + p.first;
            int next_col = col + p.second;
            if (next_row >= 0 && next_row < rooms.size() && next_col >= 0 && next_col < rooms[0].size() && rooms[next_row][next_col] > rooms[row][col])
                dfs(rooms, next_row, next_col, distance + 1);
        }
    }
};