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
            num1 = curr.val
            num2 = curr.next.val
            gcd = GCD(num1, num2)
            dummy = curr.next
            curr.next = ListNode(gcd)
            curr.next.next = dummy
            curr = curr.next.next
        return head
        