class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ans = dict()
        for x in s:
            ans[x] = ans.get(x, 0) + 1
        for x in t:
            if x not in ans:
                return False
            ans[x] = ans[x] - 1
        for x, y in ans.items():
            if y != 0:
                return False
        return True
