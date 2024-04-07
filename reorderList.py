# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Neetcode solution

class Solution(object):
    def reorderList(self, head):

        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # finding median
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next

        # reversing second part of linked list
        sec = slow.next
        slow.next = None
        prev = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp

        l1 = head # list from start without reversed list
        l2 = prev # reversed list wihout start part
        while l2 and l1:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
