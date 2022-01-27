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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr){
            return list2;
        }
        if(list2 == nullptr){
            return list1;
        }
        auto *head = list1->val > list2->val ? new ListNode(list2->val):new ListNode(list1->val);
        auto *tail = head;
        if(list1->val > list2->val){
            list2 = list2->next;
        }
        else{
            list1 = list1->next;
        }
        
        while(list1 != nullptr && list2 != nullptr){
            if(list1->val > list2->val){
                auto *ne = new ListNode(list2->val);
                tail->next = ne;
                tail = ne;
                list2 = list2->next;
            }
            else{
                auto *ne = new ListNode(list1->val);
                tail->next = ne;
                tail = ne;
                list1 = list1->next;
            }
        }
        if(list1 != nullptr){
            tail->next = list1;
        }
        else{
            tail->next = list2;
        }
        return head;
        
    }
};