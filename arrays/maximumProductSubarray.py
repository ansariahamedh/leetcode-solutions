from typing import List
class Solution:
     def maxSubArray(self, nums: List[int]) -> int:

        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]

        for num in nums[1:]:
            candidates = (num, curMax * num, curMin * num)
            curMax = max(candidates)
            curMin = min(candidates)
            result = max(result, curMax)

        return result