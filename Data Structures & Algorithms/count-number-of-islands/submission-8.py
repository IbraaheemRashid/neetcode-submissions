class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we can do dfs
        # go through eahc row and column
        # if its a 1 then we do dp on eahc direction until its either in visited or a 0
        # return the overall count

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        directions = [1,0], [-1,0], [0,1], [0,-1]

        def dfs(r, c):
            if (r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        return count
