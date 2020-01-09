class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for x in range(len(A)):
            i = 0
            j = len(A[0]) - 1
            while i <= j:
                A[x][i], A[x][j] = 1 - A[x][j], 1 - A[x][i]
                i += 1
                j -= 1
        return A

