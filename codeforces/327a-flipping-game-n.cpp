#include <bits/stdc++.h>
using namespace std;
 
void solve() {
	int n; cin >> n;
	vector<int> arr(n);
	for(auto &x : arr) cin >> x;
	int b = accumulate(arr.begin(), arr.end(), 0);
	int bg = -1; int cur = 0;
	for (auto i = 0; i < n; ++i) {
		cur += (arr[i]==0?1:-1);
		bg = max(bg, cur);
		if (cur < 0) cur = 0;		
	}
	cout << b + bg << endl;
}
 
int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}