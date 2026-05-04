# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            LeftMax=dfs(root.left)
            RightMax=dfs(root.right)
            LeftMax=(max(LeftMax,0))
            RightMax=max(RightMax,0)
            res[0]= max(res[0] ,root.val+LeftMax+RightMax)
            return root.val +max(LeftMax,RightMax)



        dfs(root)
        return res[0]

        