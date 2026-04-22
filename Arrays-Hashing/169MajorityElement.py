from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxcount = res = 0
        for num in nums:
            count[num] += 1
            if maxcount < count[num]:
                res = num
                maxcount = count[num]
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3])) # 3
    print(s.majorityElement([2,2,1,1,1,2,2])) # 2