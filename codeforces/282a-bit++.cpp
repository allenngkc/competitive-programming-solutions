#include <bits/stdc++.h>
using namespace std;

void solve() {
	int x = 0; int input;
	cin >> input;
	for (int i = 0; i < input; ++i) {
		string oper; cin >> oper;
		if (oper.find("++") != string::npos) x++;
		else x--;
	}
	cout << x << endl;
}

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}