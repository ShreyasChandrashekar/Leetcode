from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
    
# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl
print(solution.longestCommonPrefix(["dog","racecar","car"]))  # Output: ""

# Algorithm:
# 1. We iterate through each character index of the first string in the list.
# 2. For each character index, we check if all strings in the list have the same character at that index.
# 3. If we find a mismatch or if any string is shorter than the current index, 
# we return the substring of the first string up to that index as the longest common prefix.
# 4. If we finish the loop without finding any mismatches, it means the entire first string is a common prefix, so we return it.