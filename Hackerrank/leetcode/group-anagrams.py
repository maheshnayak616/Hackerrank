class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans_map = dict()
        for x in strs:
            res = ''.join(sorted(x))
            ans_map.setdefault(res, []).append(x)
        ans = list()
        for x, y in ans_map.items():
            ans.append(y)
        print ans
        return ans