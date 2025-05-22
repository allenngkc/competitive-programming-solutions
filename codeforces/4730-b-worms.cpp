#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, m; cin >> n;
	int arr[n];
	int c = 0;
	for (auto i = 0; i < n; ++i) {
		int in; cin >> in;
		c += in;
		arr[i] = c;	
	}
	cin >> m;
	for (auto loop = 0; loop < m; ++loop) {
		int w, dist = 1e9, ans; cin >> w;
		int l=0, h=n-1;	;
		while(l <= h) {
			int mid = l+(h-l)/2;
			if (w <= arr[mid]) {
				ans = mid+1; 
				h = mid-1;
			} else {
				l = mid+1;
			}
		}
		cout << ans << endl;
	}
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}