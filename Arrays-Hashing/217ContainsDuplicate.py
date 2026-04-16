from typing import List
class Solution:
     def hasDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for n in nums:
            if n in container:
                return True
            container.add(n)
        return False

# Test cases
solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 1]))  # Expected
print(solution.hasDuplicate([1, 2, 3, 4]))  # Expected: False
print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected: True


# Algorthm: Contains Duplicate
    # Use a set to track the unique elements in the array. 
    # As we iterate through the array, we check if the current element is already in the set. 
    # If it is, then we have found a duplicate and can return True. 
    # If it is not, we add the element to the set. 
    # If we finish iterating through the array without finding any duplicates, we return False.
   