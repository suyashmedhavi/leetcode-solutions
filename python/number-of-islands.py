# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid = self.convert(grid, i, j)
                    count += 1
        return count
    
    def convert(self, grid: List[List[str]], i: int, j: int) -> List[List[str]]:
        if i >= len(grid) or j >= len(grid[i]) or i < 0 or j < 0 or grid[i][j] != "1":
            return grid
        grid[i][j] = "X"
        grid = self.convert(grid, i+1, j)
        grid = self.convert(grid, i, j+1)
        grid = self.convert(grid, i-1, j)
        grid = self.convert(grid, i, j-1)
        return grid

