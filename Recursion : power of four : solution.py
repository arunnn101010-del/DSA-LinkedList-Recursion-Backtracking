# Promblem - power of four 
# Approach - bit manuplation 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffcuilty level - 342 & easy 
class Solution {
public:
    bool isPowerOfFour(int n) {
        if( n <=0) {
            return false;
        }
        return (n & (n-1)) == 0 && (n & 0x55555555) != 0;
    }
};
