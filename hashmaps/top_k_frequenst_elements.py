from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeat = {}
        answer = []
        for num in nums:
            if num in repeat:
                repeat[num] += 1
            else:
                repeat[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in repeat.items():
            bucket[freq].append(num)

        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                answer.append(num)

            if len(answer) == k:
                return answer

