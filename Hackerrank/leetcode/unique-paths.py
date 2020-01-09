class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        maze = [[0 for x in range(n) ] for x in range(m)]
        for y in range(0, n):
            for x in range(0,m):
                if x ==0 or y==0:
                    maze[x][y] = 1
                else:
                    maze[x][y] = maze[x-1][y] + maze[x][y-1]
        return maze[m-1][n-1]