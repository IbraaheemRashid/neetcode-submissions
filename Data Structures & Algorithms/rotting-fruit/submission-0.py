class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # we want to track each distance from each rotting orange
        # we add each orange to a queue
        # we go in each direction from a rotting orange
        # if itsa fresh orange that is now rotting so we add to the queue
        # we increment the minute
        # we can just return the minutes after that

        queue = deque()

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        rows,cols = len(grid), len(grid[0])

        fresh = 0
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        while fresh > 0 and queue:
            level_size = len(queue)

            for _ in range(level_size):

                r, c = queue.popleft()



                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -=1
            minutes += 1

        
        return minutes if fresh == 0 else -1
