# Promblem - reverse linked list 
# Appraoch - Three pointers 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 206 & hard
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next = NULL;

        while(curr != NULL) {
            next = curr->next;
            curr->next = prev;

            prev = curr;
            curr = next;
        }
        return prev;
    }
