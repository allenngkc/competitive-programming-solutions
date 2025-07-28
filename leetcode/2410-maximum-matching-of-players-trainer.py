class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n, m, l, ans = len(players), len(trainers), 0, 0
        for r in range(m):
            if l >= n: return ans
            if trainers[r] >= players[l]:
                l, ans = l+1, ans+1
        return ans

                