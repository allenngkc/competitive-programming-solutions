class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0]+nums[1]+nums[2], dist = abs(nums[0]+nums[1]+nums[2] - target);
        int n = nums.size();
        for (auto i = 0; i < n-2; ++i) {
            int l = i+1, r = n-1;
            while (l < r) {
                int c = nums[i] + nums[l] + nums[r];
                if (abs(c-target) < dist) {
                    dist = abs(c-target);
                    res = c;
                }
                if (c < target) l++;
                else r--;
            }
        } 
        return res;
    }
};