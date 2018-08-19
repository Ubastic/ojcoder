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
        
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        def advanceSteps(head, n):
            while n:
                head = head.next
                n -= 1
            return head
            
        lenA = getLength(headA)
        lenB = getLength(headB)
        if lenA > lenB:
            headA = advanceSteps(headA, lenA - lenB)
        elif lenA < lenB:
            headB = advanceSteps(headB, lenB - lenA)
            
        while headA:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None