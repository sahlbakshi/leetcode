# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node = head
        nodes = set()
        while node:
            if node in nodes:
                return True
            nodes.add(node)
            node = node.next
        return False
