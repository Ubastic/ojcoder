public class Solution {
    
    private static final char X = 'X';
    
    public int countBattleships(char[][] board) {
        int count = 0;
        for (int x = 0; x < board.length; x++) {
            for (int y = 0; y < board[0].length; y++) {
                if (shouldCount(board, x, y))   count++;
            }
        }
        return count;
    }
    
    private boolean shouldCount(char[][] board, int x, int y) {
        return hasBattleShip(board, x, y) && !hasBattleShip(board, x - 1, y) && !hasBattleShip(board, x, y - 1);
    }
    
    private boolean hasBattleShip(char[][] board, int x, int y) {
        if (x < 0 || y < 0) return false;
        return board[x][y] == X;
    }

}