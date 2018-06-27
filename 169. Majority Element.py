class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first method
        """
        Dict = {}
        for i in nums:
            Dict[i] = Dict.get(i,0)+1
            if (Dict[i] > len(nums)/2):
                return i
        """
        #second method 
        nums.sort()
        i = int(len(nums)/2)
        return nums[i]