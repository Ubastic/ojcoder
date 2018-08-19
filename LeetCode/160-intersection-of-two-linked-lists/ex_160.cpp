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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        if (lenA > lenB) {
            headA = advanceSteps(headA, lenA - lenB);
        } else if (lenA < lenB) {
            headB = advanceSteps(headB, lenB - lenA);
        }
        while (headA != NULL) {
            if (headA->val == headB->val)     return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }

private:
    int getLength(ListNode *head) {
        int length = 0;
        while (head != NULL) {
            ++length;
            head = head->next;
        }
        return length;
    }
    ListNode* advanceSteps(ListNode *head, int n) {
        while (n != 0) {
            head = head->next;
            --n;
        }
        return head;
    }
};