class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        res = sys.maxsize
        neighbors = {(i,j) for i in range(-1,2) for j in range(-1,2)}
        inbound = lambda x,y : 0 <= x <  len(grid) and 0 <= y < len(grid[0])
        
        if grid[0][0] != 0:
            return -1
        
        queue = deque([(0,0,1)])
        grid[0][0] = 1
        
        while queue:
            poped = queue.popleft()
            
            if poped[0] == len(grid)-1 and poped[1] == len(grid[0]) - 1:
                res = min(res,poped[2])
            
            for r,c in neighbors:
                new_row = poped[0]+r
                new_col = poped[1]+c
                if inbound(new_row,new_col) and grid[new_row][new_col] == 0:
                    queue.append((new_row,new_col,poped[2] + 1))
                    grid[new_row][new_col] = 1
        
        return -1 if res == sys.maxsize else res
            
            
            