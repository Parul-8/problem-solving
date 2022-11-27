class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def solve(board,row,cols,diag,antidiag):
            
            #basecondition
            if row == len(board):
                return 1
            count = 0
            for col in range(len(board)):
                if(cols[col]==False and diag[row-col+n-1]==False and antidiag[row+col] == False):
                    board[row][col] = 1
                    cols[col] = True
                    diag[row-col+n-1] = True 
                    antidiag[row+col] = True
                    count += solve(board,row+1,cols,diag,antidiag)
                    
                    #backtrack
                    board[row][col] = 0
                    cols[col] = False
                    diag[row-col+n-1] = False 
                    antidiag[row+col] = False
                    
            return count 
                    
                    
        
        
        board = [[0] * n for _ in range(n)]
        cols = [False] * n 
        diag = [False] * (2*n-1)
        antidiag = [False] * (2*n-1)
        
        return solve(board,0,cols,diag,antidiag)
        