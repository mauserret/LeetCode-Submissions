# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res == res[::-1]
        