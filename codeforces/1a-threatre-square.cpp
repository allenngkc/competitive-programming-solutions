#include <bits/stdc++.h>
#include <cmath>
using namespace std;

void solve() {
	double n, m, a; cin >> n >> m >> a;
	long long nn, mm;
	nn = ceil(n/a); mm = ceil(m/a);
	cout << nn * mm << endl;
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}