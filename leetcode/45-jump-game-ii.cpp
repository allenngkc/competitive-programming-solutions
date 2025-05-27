class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp;
        for(auto i = 0; i < n; ++i) {
            dp.push_back(i);
        }
        for (auto i = 0; i < n; ++i) {
            for (auto j = 1; j < nums[i]+1; ++j) {
                if (i+j >= n) continue;
                dp[i+j] = min(dp[i+j], dp[i]+1);
            }
        }
        for (auto i : dp) {
            cout << i << " ";
        }
        cout << endl;
        return dp[n-1];
    }
};