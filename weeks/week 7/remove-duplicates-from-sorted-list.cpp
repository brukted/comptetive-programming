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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == nullptr){
            return head;
        }
        auto *tail = head;
        auto *j = head;
        while(j!=nullptr){
            if(j->val != tail->val){
                tail->next = j;
                tail = tail->next;
                 j = j->next;
            }
            else{
                auto *f = j;
                j= j->next;
                // delete f;
            }
        }
        tail->next = nullptr;
        return head;
    }
};