class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        ans = list()
        text_split = text.split(" ")
        for i, key in enumerate(text_split):
            if text_split[i] == first and text_split[i + 1] == second and i < len(text_split) - 2:
                ans.append(text_split[i + 2])
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.findOcurrences("alice is a good girl she is a good student", first="a", second="good")
    print ans
    ans = s.findOcurrences("we will we will rock you", first="we", second="will")
    print ans
