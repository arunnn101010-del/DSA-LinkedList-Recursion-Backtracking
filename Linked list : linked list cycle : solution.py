# Promblem - linked list cycle 
# Appraoch - cycle detection & two pointers
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 141 & easy 
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast) {
                return true;
            }
        }
        return false;
    }
};
