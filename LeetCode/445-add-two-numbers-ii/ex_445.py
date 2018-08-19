# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rl1 = self.reverseList(l1)
        rl2 = self.reverseList(l2)
        res = self.add(rl1, rl2)
        return self.reverseList(res)
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
    def add(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        p = dummy = ListNode(-1)
        num1 = l1
        num2 = l2
        while num1 or num2:
            r = 0
            if num1:
                r += num1.val
                num1 = num1.next
            if num2:
                r += num2.val
                num2 = num2.next
            r += carry
            carry = r / 10
            digit = ListNode(r % 10)
            p.next = digit
            p = p.next
        if carry:
            digit = ListNode(carry)
            p.next = digit
            p = p.next
        return dummy.next