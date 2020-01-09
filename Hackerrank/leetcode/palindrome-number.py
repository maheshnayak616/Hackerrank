class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for z in range(len(x) // 2):
            if x[z] != x[(z * -1) + 1]:
                return False
        return True