class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i, j = 0,0
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i::])
        merged.extend(nums2[j::])

        if total_len % 2:
            return merged[int(total_len / 2)]
        even = total_len // 2
        total = (merged[even] + merged[even-1]) / 2
        return float(total)