def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, val in enumerate(nums):
        sec_val = target - val
        if sec_val in nums and nums.index(sec_val) != i:
            return sorted([i, nums.index(sec_val)])