class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        needed_num = 0
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in seen:
                return [i, seen[needed_num]]
            else:
                seen[nums[i]] = i
        return
