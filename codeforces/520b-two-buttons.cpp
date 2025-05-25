#include <bits/stdc++.h>
using namespace std;
 
int recur(int n, int m, int i) {
	if (n==m) return i;
	if (m < n) return n-m+i; 
	if (m%2==0) return recur(n,m/2,i+1);
	else return recur(n,m+1, i+1);
}
 
void solve() {
	int n, m; cin >> n >> m;
	cout << recur(n,m,0) << endl;
}
 
int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	solve();
	return 0;
}