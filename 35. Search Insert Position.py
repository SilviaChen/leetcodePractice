class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = 0
        l = len(nums)
        for i in range(0,l):
            if (nums[i] == target):
                flag = 1
                return i
            
        if (flag == 0):
            for j in range(0,l):
                if (target < nums[j]):
                    return j
            return l
            
                
        