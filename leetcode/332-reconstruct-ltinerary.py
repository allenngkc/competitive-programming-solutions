class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # we thought about this already datastructre good
        graph = defaultdict(list)   
        for a, b in tickets:
            heappush(graph[a], b)

        route = []

        # dfs post order
        def dfs(u):
            # we are appending the crap post order so earlier stuff gets sent later in time
            # when we reverse it
            # as in we porcess the later time first.
            while graph[u]:
                v = heappop(graph[u])  
                dfs(v)
            route.append(u)            

        dfs("JFK")
        return route[::-1]