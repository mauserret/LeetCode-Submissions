class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        tot = 0
        for i in range(len(tickets)):
            if i < k:
                tot += min(tickets[i], tickets[k])
            elif i > k:
                tot += min(tickets[i], tickets[k] - 1)
        tot += tickets[k]
        return tot