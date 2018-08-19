/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode plusOne(ListNode head) {
        ListNode prev = new ListNode(0);
        prev.next = head;
        ListNode p = head, start = prev;
        while (p != null) {
            if (p.val != 9)
                start = p;
            prev = p;
            p = p.next;
        }
        if (prev.val != 9) {
            prev.val += 1;
            return head;
        }
        else {
            start.val++;
            ListNode r = start.next;
            while (r != null) {
                r.val = 0;
                r = r.next;
            }
            return start.next == head ? start : head;
        }
    }
}