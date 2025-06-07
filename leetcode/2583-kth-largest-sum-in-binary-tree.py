# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level, q = {}, deque([(root, 0)])
        while q:
            node, l = q.popleft()
            if not node: continue
            if l not in level:
                level[l] = 0
            level[l] -= node.val
            q.append((node.left, l+1))
            q.append((node.right, l+1))
        arr = list(level.values())
        heapq.heapify(arr)
        return -1*heapq.nsmallest(k, arr)[-1] if len(arr) >=k else -1
        