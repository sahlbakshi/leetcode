# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        nodes = set()

        node = headA
        while node:
            nodes.add(node)
            node = node.next
        
        node = headB
        while node:
            if node in nodes:
                return node
            node = node.next
        
        return None
        