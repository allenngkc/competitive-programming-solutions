#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n; cin >> n;
	int arn[n];
	for(auto i = 0; i < n; ++i) cin >> arn[i];
	int m; cin >> m;
	int arm[m];
	for(auto i = 0; i < m; ++i) cin >> arm[i];
	sort(arn, arn+n); sort(arm, arm+m);
	int l = 0, r = 0, ans = 0;
	while (l < n and r < m) {
		if (abs(arn[l]-arm[r]) <= 1) {
			++l; ++r; ++ans;
		} else if (arn[l] > arm[r]) ++r;
		else ++l;
	}
	cout << ans << endl;

}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}