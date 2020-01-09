class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        curPos = points[0]

        for point in points[1:]:
            time += max(abs(curPos[0] - point[0]), abs(curPos[1] - point[1]))
            curPos = point

        return time