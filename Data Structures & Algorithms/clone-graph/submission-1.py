"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen={}

        def dfs(node):
            if node in seen:
                return seen[node]
            
            temp=Node(node.val)
            seen[node]=temp
            for neigh in node.neighbors:
                temp.neighbors.append(dfs(neigh))
            return temp

        return dfs(node) if node else None