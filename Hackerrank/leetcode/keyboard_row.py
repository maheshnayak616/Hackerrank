class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = ['e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y']
        second_row = ['a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's']
        third_row = ['b', 'c', 'm', 'n', 'v', 'x', 'z']
        is_one_row = False
        for x in words:
            l = list(set(list(x.lower())))
            if l[0] in first_row:
                is_one_row = all([y in first_row for y in l])
            elif l[0] in second_row:
                is_one_row = all([y in second_row for y in l])
            else:
                is_one_row = all([y in third_row for y in l])
        return is_one_row
