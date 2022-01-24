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
    ListNode* addTwoRec(ListNode *l1,ListNode* l2,const int carry){
        
        if(l1==nullptr && l2==nullptr){
            if(carry != 0){
                return new ListNode(carry);
            }
            return nullptr;
        }
        if(l1 == nullptr){
            auto v = l2->val + carry;
            auto * n = new ListNode(v%10);
            n->next  = addTwoRec(nullptr,l2->next,v/10);
            return n;
        }
        if(l2 == nullptr){
            auto v = l1->val + carry;
            auto *n = new ListNode(v%10);
            n->next = addTwoRec(l1->next,nullptr,v/10);
            return n;
        }
        auto t = l1->val + l2->val + carry;
        int result = t%10;
        auto* n = new ListNode(result);
        n->next = addTwoRec(l1->next,l2->next,t/10);
        return n;
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addTwoRec(l1,l2,0);
    }
};