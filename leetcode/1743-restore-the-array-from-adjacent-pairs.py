class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        hmap, visited, res = {}, set(), []
        for a, b in adjacentPairs:
            if a not in hmap: hmap[a] = []
            if b not in hmap: hmap[b] = []
            hmap[a].append(b)
            hmap[b].append(a)
        
        start = 0
        # find where to start
        for item, value in hmap.items():
            if len(value) == 1:
                start = item
                break
                
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                res.append(node)
                visited.add(node)
                for neigbour in hmap[node]:
                    stack.append(neigbour)
                
        return res