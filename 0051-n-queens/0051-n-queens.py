class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def arrangement(board):
            #matrix--> list with each row as its elements--> list into list
            lst=[]
            for row in board:
                lst.append(''.join(row))
            return lst
        
        def solve(board,row,cols,diag,antidiag):
            #base condition
            if row == n:
                ans.append(arrangement(board))
                return 
            
            for col in range(n):
                if(cols[col] == False and diag[row-col+n-1] == False and antidiag[row+col] == False):
                    board[row][col] = 'Q'
                    cols[col] = True
                    diag[row-col+n-1] = True
                    antidiag[row+col] = True
                    solve(board,row+1,cols,diag,antidiag)
                    
                    #backtrack
                    
                    board[row][col] = '.'
                    cols[col] = False
                    diag[row-col+n-1] = False
                    antidiag[row+col] = False
                     
        
        ans = []
        board = [['.'] * n for _ in range(n)]
        cols = [False] * n
        diag = [False] * (2*n-1)
        antidiag = [False] * (2*n-1)
        solve(board,0,cols,diag,antidiag)
        return ans
        