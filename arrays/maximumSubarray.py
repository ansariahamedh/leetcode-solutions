from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = float('-inf')
        sum = 0

        for num in nums:
            sum += num
            if sum > largestSum:
                largestSum = sum
            if sum < 0:
                sum = 0
        return largestSum