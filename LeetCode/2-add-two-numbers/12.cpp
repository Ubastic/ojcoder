/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode dummy = ListNode(-1), *p = &dummy;
        while (l1 != NULL || l2 != NULL) {
            int s = 0;
            if (l1 != NULL) {
                s += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                s += l2->val;
                l2 = l2->next;
            }
            s += carry;
            ListNode* node = new ListNode(s % 10);
            carry = s / 10;
            p->next = node;
            p = p->next;
        }
        if (carry)
            p->next = new ListNode(carry);
        return dummy.next;
    }
};