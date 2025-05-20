#include <bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	cin.exceptions(cin.failbit);
	int input; cin >> input;
	for (int i = 0; i < input; ++i) {
		string a; cin >> a;
		if (a.length() <= 10) {
			cout << a << endl;
			continue;
		} else {
			string b = a[0] + to_string(a.length()-2) + a[a.length()-1];
			cout << b << endl; 
		}
	}
	return 0;
}