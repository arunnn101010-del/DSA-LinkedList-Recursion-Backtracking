# Promblem - remove linked list element 
# Appraoch - linked list traversal + dummy LL
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 203 & Easy 
class Solution {
public:

    ListNode* removeElements(ListNode* head, int val) {

        ListNode dummy(0);

        dummy.next = head;

        ListNode* curr = &dummy;

        while(curr->next) {

            if(curr->next->val == val) {

                curr->next = curr->next->next;
            }

            else {

                curr = curr->next;
            }
        }

        return dummy.next;
    }
};
