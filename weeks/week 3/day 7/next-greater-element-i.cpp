// https://leetcode.com/problems/next-greater-element-i/

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        std::unordered_map<int,int> greater;
        std::stack<int> stack;
        
        for(const auto i : nums2){
            if(stack.size() == 0){
                stack.push(i);
                continue;
            }
            if  (i > stack.top()){
                while ((stack.size() != 0) && i > stack.top()){
                    greater[stack.top()] = i;
                    stack.pop();
                }
            }
            stack.push(i);
        }
        
        while(!stack.empty()){
            greater[stack.top()] = -1;
            stack.pop();
        }
        std::vector<int> result;
        result.reserve(nums1.size());
        for (const auto i : nums1){
            result.emplace_back(greater[i]);
        }
        return result;
    }
};