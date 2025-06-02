"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        data, q = {}, deque([(root,0)])
        while q:
            node, level = q.popleft()
            for c in node.children:
                q.append((c, level+1))
            if level not in data:
                data[level] = [node.val]
            else:
                data[level].append(node.val)
        return list(data.values())
        