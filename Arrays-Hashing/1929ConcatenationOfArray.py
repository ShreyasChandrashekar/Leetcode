# Algorithm: Concatenation of Array
# Time Complexity: O(n)
# Space Complexity: O(1) (in-place modification)

# Use Slicing to concatenate the array by appending a copy of the original array to itself.
# If m is the length of the original array, we can assign the elements from index m to m-1 on one side
# to the elements from index 0 to m-1 on the other side, effectively doubling the array in place.

from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        m = len(nums)
        nums[m:] = nums[:m]
        return nums
    
# Test cases
solution = Solution()
print(solution.getConcatenation([1, 2, 1]))        # Expected: [1, 2, 1, 1, 2, 1]
print(solution.getConcatenation([1, 3, 2, 1]))     # Expected: [1, 3, 2, 1, 1, 3, 2, 1]