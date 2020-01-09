class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not  len(strs):
            return ""
        smallest = min(strs, key=len)
        strs.remove(smallest)
        for y in strs:
            found = False
            new_pattern = ""
            for x in smallest:
                new_pattern += x
                if y.startswith(new_pattern):
                    found = True
                else:
                    new_pattern = new_pattern[:-1]
                    break
            if not found:
                smallest = ""
                break
            smallest = new_pattern

        return smallest