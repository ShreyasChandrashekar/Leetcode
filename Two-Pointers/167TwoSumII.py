from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1
        res = []
        while l < r:
            tot = nums[l] + nums[r]

            if tot < target:
                l+=1
            elif tot > target:
                r-=1
            else:
                return [l+1,r+1]