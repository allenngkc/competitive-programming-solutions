#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, k; cin >> n >> k;
	int arr[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}	
	int threshold = arr[k-1];
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (arr[i] >= threshold && arr[i] > 0) res++;
	}
	cout << res << endl;
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}