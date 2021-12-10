// https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        auto less_nums = 0;
        auto count = 0;
        
        for(auto i : nums){
            if(i<target){
                ++less_nums;
            }
            else if(i==target){
                ++count;
            }
        }
        
        vector<int> indices;
        indices.reserve(count);
        while(count != 0){
            indices.push_back(less_nums++);
            --count;
        }
        return std::move(indices);
    }
};