from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        spaces = len(height) - 1
        maxArea = 0
        while(l < r):
            area = 0
            if height[l] < height[r] or height[l] == height[r]:
                area = height[l] * spaces
                maxArea = max(area,maxArea)
                l+=1
                spaces-=1
            elif height[l] > height[r]:
                area = height[r] * spaces
                maxArea = max(area,maxArea)
                r-=1
                spaces-=1
        
        return maxArea




        