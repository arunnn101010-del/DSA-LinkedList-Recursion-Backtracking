# Promblem - power of three 
# Approach - division 
# Time and space complexity - 0(log3 n) & 0(1)
# Leetcode and diffculty level - 326 & easy 
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n <= 0) {
            return false;
        }
        while(n % 3 == 0) {
            n = n / 3;
        }
        return n == 1;
    }
};
