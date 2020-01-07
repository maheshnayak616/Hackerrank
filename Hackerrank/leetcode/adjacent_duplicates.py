class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for x in S:
            if not stack:
                stack.append(x)
            else:
                y = stack.pop()
                if x != y:
                    stack.append(y)
                    stack.append(x)
        print "".join(stack)

if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates("abbaca")