# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:    return
        p = head
        while p:
            dup = RandomListNode(p.label)
            dup.next = p.next
            p.next = dup
            p = dup.next
        p = head
        while p:
            dup = p.next
            if p.random:
                dup.random = p.random.next
            p = dup.next
        p = head
        dup_head = head.next
        while p:
            dup = p.next
            p.next = dup.next
            if dup.next:
                dup.next = dup.next.next
            p = p.next
        return dup_head