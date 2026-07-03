from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = par[n]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

        return []
    
# Example usage:

# Input: [[1,2],[1,3],[2,3]]
# Output: [2,3]
solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
print(solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

# Time Complexity: O(E * α(V)), where E is the number of edges and α is the inverse Ackermann function, which grows very slowly.
# Space Complexity: O(V), where V is the number of vertices, for storing the parent and rank arrays.