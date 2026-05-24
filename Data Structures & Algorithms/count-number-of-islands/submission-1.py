class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # go through the whole matrix and look for 1s
        # once we get to a 1, we increment and we want to check each direction if that's a 1
        # if it is then do the same thing otherwise return 
        # if its out of bounds or a 0 or we've seen it before we dont want to check

        # we do this using dfs

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows, cols = len(grid), len(grid[0])

        visited = set()

        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    dfs(row, col)
        
        return res
