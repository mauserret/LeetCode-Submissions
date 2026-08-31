class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        pivot_list = []
        higher = []
        for num in nums:
            if num == pivot:
                pivot_list.append(num)
            elif num < pivot:
                lower.append(num)
            else:
                higher.append(num)
        return lower + pivot_list + higher

        