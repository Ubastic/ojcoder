/**
 * Definition for ListNode
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
    /**
     * @param ListNode head is the head of the linked list 
     * @oaram m and n
     * @return: The head of the reversed ListNode
     */
    public ListNode reverseBetween(ListNode head, int m , int n) {
        // write your code
        if(head == null || m == n) return head;
        
        int index = 1;
        ListNode pre = head;
        
        while(index < m - 1){
            pre = pre.next;
            index++;
        }
        
        ListNode start = m == 1 ? head : pre.next, end = m == 1 ? head : pre.next;
        
        n += m == 1 ? 1 : 0;
        
        while(index < n - 1){
            ListNode toInsert = end.next;
            end.next = toInsert.next;
            if(m != 1) pre.next = toInsert;
            toInsert.next = start;
            start = toInsert;
            index++;
        }
        
        return m == 1 ? start : head;
    }
}
