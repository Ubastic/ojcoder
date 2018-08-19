# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0)
        prev.next = head
        p = head
        start = prev
        while p:
            if p.val != 9:
                start = p
            prev = p
            p = p.next
        if prev.val != 9:
            prev.val += 1
            return head
        else:
            start.val += 1
            r = start.next
            while r:
                r.val = 0
                r = r.next
            return start if start.next == head else head