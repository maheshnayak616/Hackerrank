class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x ==0 and y== 0:
                    dp[x][y] = grid[x][y]
                elif x == 0:
                    dp[x][y] = dp[x][y - 1] + grid[x][y]
                elif y == 0:
                    dp[x][y] = dp[x -1][y] + grid[x][y]
                else:
                    dp[x][y] = min(dp[x][y-1], dp[x-1][y]) + grid[x][y]
        return dp[len(grid) - 1][len(grid[0]) - 1]