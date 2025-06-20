class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q, v = deque([("0000", 0)]), set(deadends)
        if "0000" in deadends: return -1
        DIR = [-1, 1]
        while q:
            node, moves = q.popleft()
            if node == target: return moves
            for i in range(4):
                p = int(node[i])
                for k in DIR:
                    d = str((p+k) % 10)
                    new_node = node[:i] + d + node[i+1:]
                    if new_node not in v:
                        v.add(new_node)
                        q.append((new_node,moves+1))
        return -1