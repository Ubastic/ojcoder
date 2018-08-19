class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int count = 0;
        for (int i = 0; i != board.size(); ++i) {
            for (int j = 0; j != board[0].size(); ++j) {
                if (shouldCount(board, i, j))
                    ++count;
            }
        }
        return count;
    }
    
    bool hasBattleship(vector<vector<char>>& board, int x, int y) {
        if (x < 0 || y < 0)     return false;
        return board[x][y] == 'X';
    }
    
    bool shouldCount(vector<vector<char>>& board, int x, int y) {
        return hasBattleship(board, x, y) && !hasBattleship(board, x, y - 1) && !hasBattleship(board, x - 1, y);
    }
};