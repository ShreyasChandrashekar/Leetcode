class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # You are using .get() for countT to handle the case,
        # where a character in countS might not be present in countT.
        # If you do countS[c] != countT[c], it would raise a KeyError,
        # if c is not a key in countT.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

# Test cases
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
print(solution.isAnagram("rat", "car"))          # Expected: False