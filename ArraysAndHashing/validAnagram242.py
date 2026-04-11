class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        StringS, StringT = {}, {}

        for i in range(len(s)):
            StringS[s[i]] = 1 + StringS.get(s[i], 0)
            StringT[t[i]] = 1 + StringT.get(t[i], 0)
        
        for c in StringS:
            if StringS[c] != StringT.get(c, 0):
                return False

# Time Complexity Analysis

# Time Complexity : O(m+n)
# Space Complexity : O(1) Since there are only 26 letters in the English Alphabet

# Another approach to solving the above problem could be to just
# sort both the strings individually and then compare and return the sorted strings
# Time Complexity : O(nlogn + mlogm)
# Space Complexity : O(1) or O(m+n) "Depends on the sorting algorithm"

# The below is for my understanding as to how dicionary works and iterates

# print(StringS.items())
# print(StringT.items())

# for c in StringS:
#     print("This is the value of C", c)
#     print("This is the value of StringS",StringS[c])
#     print("\n")