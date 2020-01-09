class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,p = 0,1

        while n:
            x = n % 10
            r = n // 10
            s += x
            p *= x
            n = r
        return p - s