class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = nums.count(0)
        while 0 in nums:
             nums.remove(0)
        while (counter):
            counter-=1
            nums.append(0)
        