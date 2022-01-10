// https://leetcode.com/problems/power-of-four/

class Solution {
    fun isPowerOfFour(n: Int): Boolean =
    if (n == 1){
        true
    }
    else if (n == 0 || n % 4 != 0) {
        false
    } else {
        isPowerOfFour((n / 4))
    }   
}