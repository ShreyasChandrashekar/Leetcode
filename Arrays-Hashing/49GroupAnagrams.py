from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        k = ""
        for s in strs:
            k = "".join(sorted(s))
            res[k].append(s)
        return list(res.values())

# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(s.groupAnagrams([""])) # [[""]]
    print(s.groupAnagrams(["a"])) # [["a"]]