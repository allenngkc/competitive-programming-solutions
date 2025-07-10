class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        int l = 0, res = 0;

        for (auto r = 0; r < nums.size(); r++) {
            if (freq.find(nums[r]) == freq.end()) freq[nums[r]] = 0;
            freq[nums[r]] += 1;

            while (freq[nums[r]] > k) {
                freq[nums[l]] -= 1;
                l += 1;
            }

            res = max(res, r-l+1);
        }
        return res;
    }
};