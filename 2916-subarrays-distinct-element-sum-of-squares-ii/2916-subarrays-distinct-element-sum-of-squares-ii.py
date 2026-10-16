class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, start, end, val):
            length = end - start + 1
            tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + length * val * val) % MOD
            tree_sum[node] = (tree_sum[node] + length * val) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            if lazy[node]:
                mid = (start + end) // 2
                apply(2 * node, start, mid, lazy[node])
                apply(2 * node + 1, mid + 1, end, lazy[node])
                lazy[node] = 0

        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                apply(node, start, end, val)
                return

            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)

            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        last_pos = {}
        ans = 0

        for j, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            update(1, 0, n - 1, prev + 1, j, 1)
            ans = (ans + tree_sq[1]) % MOD
            last_pos[val] = j

        return ans