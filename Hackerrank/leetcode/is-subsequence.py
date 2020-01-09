class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        s = s.strip()
        if not s :
            return True
        for c in t:
            if c == s[j]:
                j += 1
            if j == len(s):
                return True
        return False
