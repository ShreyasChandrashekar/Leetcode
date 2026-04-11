class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        m = len(nums)
        nums[m:] = nums[:m]
        return nums
    
# Test cases
solution = Solution()
print(solution.getConcatenation([1, 2, 1]))        # Expected: [1, 2, 1, 1, 2, 1]
print(solution.getConcatenation([1, 3, 2, 1]))     # Expected: [1, 3, 2, 1, 1, 3, 2, 1]