# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(n1, n2):
            res = min(n1, n2)

            while res > 0:
                if n1 % res == 0 and n2 % res == 0:
                    return res
                res -= 1

        curr = head
        while curr.next:  
            dummy = curr.next
            curr.next = ListNode(GCD(curr.val, curr.next.val))
            curr.next.next = dummy
            curr = curr.next.next
        return head
        