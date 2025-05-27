class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int sum = 0, l = 0, r = arr.size()-1;
        for(auto i : arr) sum += i;
        int cl = 0, cr = 0;
        while (l < r && r-l > 1) {
            cl += arr[l];
            if (3*cl == sum) {
                int tr = r, tcr = cr;
                while (tr-l > 1) {
                    tcr += arr[tr];
                    --tr;
                    if (cl==tcr) return true;
                }
            }
            ++l;
        }
        return false;
    }
};