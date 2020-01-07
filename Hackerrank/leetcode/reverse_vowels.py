class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i, j = 0, len(s) - 1
        while i < j:

            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
            elif s[i] in vowels:
                j -= 1
            else:
                i += 1
        return "".join(s)

if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels("leetcode")