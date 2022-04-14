/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        auto* i = head;
        auto* j = i;
        auto* min = i;
        
        while(i != nullptr){
            j = i;
            min = i;
            while(j != nullptr){
                if (j->val < min->val) {
                    min = j;
                }
                j = j->next;
            }
            const auto t = min->val;
            min->val = i->val;
            i->val = t;
            i = i->next;
        }
        
        return head;
    }
};
