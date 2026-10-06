class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        for num in nums:
            current_sum += num
            difference = current_sum - k

            count += hashmap[difference]
            hashmap[current_sum] += 1
        return count
