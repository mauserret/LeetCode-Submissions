class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot_sum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        for num in nums:
            tot_sum += num
            prefix_sum = tot_sum - k

            if prefix_sum in hashmap:
                count += hashmap[prefix_sum]
            hashmap[tot_sum] += 1
        return count
