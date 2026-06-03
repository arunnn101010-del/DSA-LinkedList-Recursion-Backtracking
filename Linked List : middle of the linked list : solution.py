# Promblem - middle of the linked list 
# Approach - Two pointers
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 876 & easy 
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
