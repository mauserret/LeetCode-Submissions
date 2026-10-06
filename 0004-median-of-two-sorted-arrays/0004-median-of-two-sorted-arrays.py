class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        total_len = len(merged)
        if total_len % 2:
            return merged[total_len // 2]
        return (merged[total_len // 2 - 1] + merged[total_len // 2]) / 2