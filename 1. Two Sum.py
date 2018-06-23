class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #one method
        """
        i = j = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[j] == target-nums[i]): 
                    return [i, j]
        """
        #second method
        key = {}
        i = 0
        for i in range(len(nums)):
            if target - nums[i] in key:
                return [key[target - nums[i]], i]
            if nums[i] not in key:
                key[nums[i]] = is