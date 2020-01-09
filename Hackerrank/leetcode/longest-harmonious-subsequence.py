class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        y = dict()
        for x in range(len(nums)):
            y[nums[x]] = y.get(nums[x], 0) + 1
        max_val = 0
        for x, z in y.items():
            if x - 1 in y and max_val < z + y[x-1]:
                max_val = z + y[x-1]
        return max_val
