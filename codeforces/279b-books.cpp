#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, t; cin >> n >> t;
	int arr[n];
	for (auto i = 0; i < n; ++i) cin >> arr[i];
	int l = 0; int r = 0; int res = 0;
	while (r < n) {
		if (arr[r] <= t) {
			t -= arr[r];
			res = max(res,r-l+1);
			++r;
		} else {
			
			t += arr[l];
			++l;
			
		}
	}
	cout << res << endl;
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}