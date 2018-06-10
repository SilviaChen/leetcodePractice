class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        sum = 0
        totalLen = len(nums)
        for i in range(0,totalLen,2):
            sum += nums[i]
        return sum