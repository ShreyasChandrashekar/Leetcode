class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s) # You are converting the count list into a tuple because lists cannot be keys in dictionaries
        
        return list(res.values())
    
# Time Complexity Analysis

# Time Complexity : O(m * n)  Where m is the number of strings and n is the length of the longest string.
# Space Complexity : O(m)

# Visually Below is how your Dictionary would finally look like when you return the list of values

# strs = ["eat","tea","tan","ate","nat","bat"]
# res = {                                     KEYS                                               VALUES
#         a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.
#        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : ["ate","eat","tea"]
#        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : ["nat","tan"]
#        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : ["bat"]
# }

# strs = ["act","pots","tops","cat","stop","hat"]
# res = {                                     KEYS                                               VALUES
#         a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
#        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : ["act", "cat"]
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0] : ["stop", "pots", "tops"
#        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : ["hat"]
# }