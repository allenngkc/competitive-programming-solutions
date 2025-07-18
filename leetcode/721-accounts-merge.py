class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n, aura, lookup = len(accounts), {}, {}
        
        for i in range(n):
            aura[i] = set(accounts[i][1:])
        for i in range(n):
            for j in accounts[i][1:]:
                if j not in lookup:
                    lookup[j] = i
                elif j in lookup and i != lookup[j]:
                    o = lookup[j]
                    for e in aura[lookup[j]]:
                        lookup[e] = i
                        aura[i].add(e)
                    del aura[o]
        ans = []
        for k, v in aura.items():
            emails = list(v)
            emails.sort()
            curr = [accounts[k][0]] + emails
            ans.append(curr)
        return ans