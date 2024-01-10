class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0
        visited = []

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            
            grid[r][c] = '0'
            
            for i in range(4):
                dfs(r + dx[i], c + dy[i])
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                
                cnt += 1
                dfs(r, c)
        
        return cnt