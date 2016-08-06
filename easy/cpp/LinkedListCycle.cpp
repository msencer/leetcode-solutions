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
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        
        ListNode* fast = head->next;
        while(fast != NULL){
            if(head == fast) return true;
            
            fast = fast->next;
            if (fast == NULL) break;
            fast = fast->next;
            head = head->next;
        }
        return false;
    }
};