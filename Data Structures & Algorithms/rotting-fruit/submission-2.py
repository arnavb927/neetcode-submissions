class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        def helper(i, j, queue):
            if 0 <= i+1 < rows:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append([i+1, j])
            if 0 <= i-1 < rows:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append([i-1, j])
            if 0 <= j+1 < cols:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append([i, j+1])
            if 0 <= j-1 < cols:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append([i, j-1])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])
        time = -1

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                helper(row, col, queue)
            time += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return max(time, 0)


