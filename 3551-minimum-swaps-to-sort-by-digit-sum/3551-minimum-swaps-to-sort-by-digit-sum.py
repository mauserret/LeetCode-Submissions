class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(num: int) -> int:
            return sum(int(d) for d in str(num))

        arr = [(get_digit_sum(num), num, i) for i, num in enumerate(nums)]
        arr.sort()

        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
            
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
            if cycle_size > 0:
                swaps += (cycle_size - 1)
        return swaps




