class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (int)(len(nums)*(len(nums)+1))/2
        return int(total - sum(nums))