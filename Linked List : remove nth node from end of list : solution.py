# Promblem - remove nth node feom end of list 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 19 & medium 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode* slow = &dummy;
        ListNode* fast = &dummy;

        for(int i=0; i<=n; i++) {
            fast = fast->next;
        }
        while(fast) {
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next;

        return dummy.next;
    }
};
