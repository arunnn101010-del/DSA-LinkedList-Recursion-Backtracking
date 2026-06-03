# Promblem - intersection of two linked list 
# Approach - two pointers
# Time and space complexity - 0(n+m) & 0(1)
# Leetcode and diffculty level - 160 & easy 
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* pA = headA;
        ListNode* pB = headB;

        while(pA != pB) {
            pA = (pA == NULL) ? headB : pA->next;
            pB = (pB == NULL) ? headA : pB->next;
        }
        return pA;
    }
};
