#include <bits/stdc++.h>
using namespace std;

void solve() {
	vector<char> vowels = {'a', 'e', 'i', 'o', 'u', 'y'};
	string str, res; cin >> str;
	for (auto i = 0; i < str.length(); ++i) {
		if (find(vowels.begin(), vowels.end(), tolower(str[i], locale())) == vowels.end()) {
			res += '.';
			res += char(tolower(str[i]));
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