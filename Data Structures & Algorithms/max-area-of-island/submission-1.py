class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same thing do dfs
        directions = [0,1], [0, -1], [1,0],[-1,0]

        rows = len(grid)
        cols = len(grid[0])

        maxCount = 0

        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 0

            area = 1
            grid[row][col] = 0

            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            
            return area

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxCount = max(maxCount, dfs(row, col))
        
        return maxCount

            