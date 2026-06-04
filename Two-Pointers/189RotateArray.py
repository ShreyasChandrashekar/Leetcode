from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        
        # Reverse the whole array first
        l , r = 0, len(nums)-1
        reverse(l,r,nums)
        
        # Reverse the k value elements in the array
        l , r = 0, k-1
        reverse(l,r,nums)
        
        # Reverse the rest of the elements after k
        l , r = k, len(nums)-1
        reverse(l,r,nums)