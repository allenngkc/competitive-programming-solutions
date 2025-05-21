#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, l; cin >> n >> l;
	double arr[n];
	for (auto i = 0; i < n; ++i) cin >> arr[i];
	sort(arr, arr+n);
	double res = max(arr[0], l-arr[n-1]);
	for (auto i = 0; i < n-1; ++i) {
		res = max(res, (arr[i+1]-arr[i])/2.0);
	}
	cout << fixed << setprecision(10) << res << endl;
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}