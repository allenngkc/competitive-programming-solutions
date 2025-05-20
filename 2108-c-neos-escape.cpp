#include <bits/stdc++.h>
using namespace std;

void solve() {
	int c; cin >> c;
	for (auto i = 0; i < c; ++i) {
		int n, prev; cin >> n;
		int res = 0;
		vector<int> clean;
		prev = -1;
		for (auto j = 0; j < n; ++j) {
			int curr; cin >> curr;
			if (prev != curr) {
				prev = curr;
				clean.push_back(curr);
			}
		}
		if (clean.size() == 1) {
			cout << 1 << endl;
			continue;
		}
		for(auto i = 0; i < clean.size(); ++i) {
			if (i-1 >= 0 && i+1 < clean.size()) {
				if (clean[i-1] < clean[i] && clean[i] > clean[i+1]) ++res;
			} else if (i-1 >= 0 && clean[i-1] < clean[i]) ++res;
			else if (i+1 < clean.size() && clean[i+1] < clean[i]) ++res;
		}		
		cout << res << endl;
	}
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}