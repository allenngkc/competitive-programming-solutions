#include <bits/stdc++.h>
using namespace std;

void solve() {
	int tt = 1; cin >> tt;
	while(tt--) {
		int n; cin >> n;
		vector<int> a;
		a.push_back(-1e9);
		for(auto i = 0; i < n; ++i) {
			int c; cin >> c;
			if (a.back() != c) {
				a.push_back(c);
			}
		}
		a.push_back(-1e9);
		int r = 0;
		for (auto i = 1; i < a.size(); ++i) {
			if (a[i-1] < a[i] && a[i+1] < a[i]) ++r;
		}
		cout << r << endl;
	}
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}