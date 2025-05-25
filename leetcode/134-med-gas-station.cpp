class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int lev = 0; int gev = 0; int ans = 0;
        for (auto i = 0; i < gas.size(); ++i) {
            int ev = gas[i] - cost[i];
            if (lev == 0 and ev > 0) ans = i;
            lev += ev;
            if (lev < 0) {
                gev += lev;
                lev = 0;
            }
        }
        if (lev < -1 * gev) return -1;
        return ans;
    }
};