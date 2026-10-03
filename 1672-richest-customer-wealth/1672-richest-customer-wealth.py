class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_balance = 0

        for acc in accounts:
            max_balance = max(max_balance, sum(acc))
        return max_balance
        