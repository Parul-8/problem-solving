class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        cols = [set() for i in range(n)]
        rows = [set() for i in range(n)]
        boxes = [set() for i in range(n)]
        
        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if val == '.':
                    continue
                    
                if val in rows[row]:
                    return False
                rows[row].add(val)
                
                if val in cols[col]:
                    return False
                cols[col].add(val)
                
                indx = (row // 3) * 3 + col // 3
                if val in boxes[indx]:
                    return False
                boxes[indx].add(val)
        
        
        
        
        return True
    
    
    