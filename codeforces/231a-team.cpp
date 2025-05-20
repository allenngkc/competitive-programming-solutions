#include <bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int input; cin >> input;
	int res = 0;
	for (int i = 0; i < input; ++i) {
		int count = 0;
		for (int j = 0; j < 3; ++j) {
			int curr; cin >> curr;
			if (curr == 1) {count++;}
		}
		if (count >= 2) {res++;}
	}
	cout << res << endl;
	return 0;
}