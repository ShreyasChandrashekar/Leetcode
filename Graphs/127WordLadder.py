from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:

            for i in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return res
                

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neiWord in nei[pattern]:

                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            
            res+=1
        
        return 0

# Example usage:
solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
result = solution.ladderLength(beginWord, endWord, wordList)
print(result)  # Output: 5

# Time & Space Complexity:
# - Time Complexity: O(M2 * N), where M is the length of each word and N is the number of words in the wordList. We generate all possible patterns for each word and perform a BFS traversal.
# - Space Complexity: O(M2 * N), for storing the adjacency list and the visited set.

# '*ot': ['hot', 'dot', 'lot'], 
# 'h*t': ['hot', 'hit'], 
# 'ho*': ['hot'], 
# 'd*t': ['dot'], 
# 'do*': ['dot', 'dog'], 
# '*og': ['dog', 'log', 'cog'], 
# 'd*g': ['dog'], 
# 'l*t': ['lot'], 
# 'lo*': ['lot', 'log'], 
# 'l*g': ['log'], 
# 'c*g': ['cog'], 
# 'co*': ['cog'], 
# '*it': ['hit'], 
# 'hi*': ['hit']