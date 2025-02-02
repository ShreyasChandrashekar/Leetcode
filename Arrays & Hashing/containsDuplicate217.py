class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for i in nums:
            if i in container:
                return True
            elif i not in container:
                container.add(i)
        return False
    

# Time Complexity Analysis

#If you use the two pointer method i.e two loops
#then time complexity would be O(n2)

#If you use the sorting method first and then compare the elements
#then time complecity would O(nlogn)

#If you use a HashSet as shown in the above code 
#Time complexity will be O(n)
#Space complexity O(n)