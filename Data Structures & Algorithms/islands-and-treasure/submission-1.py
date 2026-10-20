class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        # use a queue to track each 0 
        # then go in each direction from each 0
        # add to the queue, this makes sense
        if not grid or not grid[0]:
            return

        queue = deque()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                
                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = 1 + grid[r][c]
                queue.append((nr, nc))
        