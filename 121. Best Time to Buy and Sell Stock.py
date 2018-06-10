class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) == 0):
            return 0
        max_price = 0
        min_price = prices[0]
        
        for i in prices:
            if (min_price > i ):
                min_price = i
            elif (i-min_price > max_price):
                max_price = i-min_price
        return max_price
                