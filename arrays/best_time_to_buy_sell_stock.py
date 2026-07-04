# Brute force O(n²)
class SolutionBrute(object):
    def maxProfit(self,prices):
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
        return maxProfit
# Optimal hashmap O(n)
class SolutionOptimal(object):
    def maxProfit(self,prices):
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit