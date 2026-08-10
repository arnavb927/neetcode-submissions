class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                
                bound_x = j//3
                bound_y = i//3
                for m in range(bound_x * 3, bound_x * 3 + 3):
                    for n in range(bound_y * 3, bound_y * 3 + 3):
                        if i == n and j == m:
                            continue
                        if board[n][m] == board[i][j]:
                            return False
                        else:
                            continue
                for n in range(9):
                    if n != j:
                        if board[i][j] == board[i][n]:
                            
                            return False
                    if n != i:
                        if board[i][j] == board[n][j]:
                            return False
        return True
