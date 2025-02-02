class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i, n in enumerate(nums):  # 'i' is the index and 'n' is the value of the array
            diff = target - n
            if diff in prevMap:    # diff will check the values 'n' in the hash map
                return [prevMap[diff] , i]
            
            prevMap[n] = i
        
        return
    
# Time Complexity Analysis

# Time Complexity : O(n) Because you will make atleast one pass on the array
# Space Complexity : O(n) Space required for the enumerate dictionary/array