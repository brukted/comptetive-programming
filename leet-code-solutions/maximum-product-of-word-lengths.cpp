class Solution {
public:
    int maxProduct(vector<string>& words) {
        auto masks = vector<int>();
        
        const auto size = words.size();
        
        masks.reserve(size);
        
        for(const auto& word : words){
            int mask = 0;
            for(auto i = 0; i< word.size(); ++i){
                mask |= 1 << ((int) word[i] - 97);
            }
            masks.push_back(mask);
        }
        
        size_t maxx = 0;
        
        for (auto i = 0; i < size; ++i){
            for( auto j = i +1 ; j < size; ++j){
                if((masks[i] & masks[j]) == 0){
                    maxx = max(words[i].size() * words[j].size(), maxx);
                }
            }
        }
        
        return maxx;
    }
};