# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def check(root, i):
            if i == len(arr): return True
            if not root: return False
            if root.val == arr[i]:
                return check(root.left, i+1) or check(root.right, i+1)
            else:
                return False

        def traverse(root):
            if not root: return False
            return check(root, 0) or traverse(root.left) or traverse(root.right)

        return traverse(root)