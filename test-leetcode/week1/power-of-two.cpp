class Solution {
public:
    bool isPowerOfTwo(int n) {
        int on_bits = 0;
        
        while(n > 0){
            if(n & 1){
                ++on_bits;
            }
            n >>= 1;
        }
        
        return on_bits == 1;
    }
};