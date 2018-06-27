class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Dict = {}
        for i in nums:
            Dict[i] = Dict.get(i, 0)+1
            
        for j in nums:     
            if (Dict[j] ==1):
                return j