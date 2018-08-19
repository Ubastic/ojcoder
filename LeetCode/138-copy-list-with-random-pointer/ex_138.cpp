/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        map<RandomListNode*, RandomListNode*> nodes;
        auto curr = head;
        while (curr) {
            auto copy = new RandomListNode(curr->label);
            nodes[curr] = copy;
            curr = curr->next;
        }
        curr = head;
        while (curr) {
            nodes[curr]->next = nodes[curr->next];
            nodes[curr]->random = nodes[curr->random];
            curr = curr->next;
        }
        return nodes[head];
    }
};