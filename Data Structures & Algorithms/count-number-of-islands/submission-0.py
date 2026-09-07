class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        col = len(grid[0])
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"

                    def helper(i, j):
                        if 0 <= i + 1 < rows:
                            if grid[i+1][j] == "1":
                                grid[i+1][j] = "0"
                                helper(i+1, j)
                        if 0 <= i - 1 < rows:
                            if grid[i-1][j] == "1":
                                grid[i-1][j] = "0"
                                helper(i-1, j)
                        if 0 <= j + 1 < col:
                            if grid[i][j+1] == "1":
                                grid[i][j+1] = "0"
                                helper(i, j+1)
                        if 0 <= j - 1 < col:
                            if grid[i][j-1] == "1":
                                grid[i][j-1] = "0"
                                helper(i, j-1)

                    helper(i, j)
        return res


