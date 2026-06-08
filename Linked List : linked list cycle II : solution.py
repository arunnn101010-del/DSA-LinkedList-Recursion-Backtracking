# Promblem - linked list cycle II 
# Approach - cycle detection 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 142 & easy 
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast) {
                ListNode* entry = head;

                while(entry != slow) {

                    entry = entry->next;
                    slow = slow->next;
                }
                return entry;
            }
        }
        return NULL;
    }
};
