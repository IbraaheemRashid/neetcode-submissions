class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(row, col, visited, prev):
            if (
                row >= rows or col >= cols or
                row < 0 or col < 0 or
                (row, col) in visited or
                heights[row][col] < prev
            ):
                return

            visited.add((row, col))

            for dr, dc in directions:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res