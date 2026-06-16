# Promblem - climbing stairs 
# Appraoch - dyanmic proagramming 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 70 & easy 
class Solution {
public:
    int climbStairs(int n) {
        
        if(n <= 2) 
            return n;

        int prev2 = 1;
        int prev1 = 2;

        for(int i=3; i <= n; i++) {
            int curr = prev1 + prev2;

            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
