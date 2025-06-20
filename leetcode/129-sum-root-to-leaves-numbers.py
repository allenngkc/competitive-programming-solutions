# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(curr, node):
            nonlocal res
            if not node: return
            curr += node.val
            if not node.left and not node.right: res += curr
            recur(curr*10,node.left)
            recur(curr*10,node.right)
        recur(0, root)
        return res