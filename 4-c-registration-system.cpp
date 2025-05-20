#include <bits/stdc++.h>
using namespace std;

void solve() {
	int tt = 0; cin >> tt;
	unordered_map<string, int> hmap;
	while(tt--) {
		string n; cin >> n;
		if (hmap.find(n) == hmap.end()) {
			hmap[n] = 1;
			cout << "OK" << endl;
		} else {
			cout << n << hmap[n] << endl;
			hmap[n]++;
		}
	}
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}