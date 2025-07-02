class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> dp;
        int n = nums.size();
        for (auto i = 0; i < n; i++) {
            dp.push_back(0);
        } 
        dp[n-1] = 1; int s = 1;
        for (auto i = n-2; i >= 0; i--) {
            if (nums[i] >= s) {s = 1; dp[i] = 1;}
            else s += 1;
        }
        return dp[0];
    }

};