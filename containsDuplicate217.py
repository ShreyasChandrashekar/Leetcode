class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for i in nums:
            if i in container:
                return True
            elif i not in container:
                container.add(i)
        return False