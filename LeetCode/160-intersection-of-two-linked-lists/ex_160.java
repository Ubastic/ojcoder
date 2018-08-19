/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        if (lenA > lenB) {
            headA = advanceSteps(headA, lenA - lenB);
        } else if (lenA < lenB) {
            headB = advanceSteps(headB, lenB - lenA);
        }
        while (headA != null) {
            if (headA.val == headB.val)     return headA;
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }

    private int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            length++;
            head = head.next;
        }
        return length;
    }

    private ListNode advanceSteps(ListNode head, int n) {
        while (n != 0) {
            head = head.next;
            n--;
        }
        return head;
    }
}