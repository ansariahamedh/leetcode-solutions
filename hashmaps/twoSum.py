# Brute force O(n²)
class SolutionBrute(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Optimal hashmap O(n)
class SolutionOptimal(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in seen:
                return [seen[find], i]
            seen[num] = i
