class Solution:
    def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        x, y = e
        
        
        is_exit = lambda i, j : i*j==0 or i==m-1 or j==n-1
        
        
        def adj(i,j, dirs=[1, 0, -1, 0, 1]):
            for d in range(4):
                ii, jj = i + dirs[d], j + dirs[d+1]
                if 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != "+":
                    yield ii,jj
            
        dq = deque([(x,y,0)])                    
        maze[x][y] = '+'                          
        while dq:                                  
            i, j, s = dq.popleft()                 
            for ii,jj in adj(i,j):                
                maze[ii][jj] = "+"                 
                if is_exit(ii,jj) : return s+1     
                dq.append((ii,jj,s+1))             
                
        return -1                                  