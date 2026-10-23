class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return 1 + search(row+1, col) + search(row-1, col) + search(row, col+1) + search(row, col-1)
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(search(row, col), max_area)
        return max_area