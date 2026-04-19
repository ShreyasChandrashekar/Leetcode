
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Test cases
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(solution.twoSum([3, 2, 4], 6))   # Expected: [1, 2]
print(solution.twoSum([3, 3], 6))   # Expected: [0, 1]