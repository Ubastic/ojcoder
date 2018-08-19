/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode p = head;
        ListNode prev = null;
        
        while (p != null) {
            ListNode next = p.next;
            p.next = prev;
            prev = p;
            p = next;
        }
        
        return prev;
    }
}