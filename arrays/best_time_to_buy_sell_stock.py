class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for num in prices:
            if num < min_price:
                min_price = num
            elif num - min_price > max_profit:
                max_profit = num - min_price
        return max_profit