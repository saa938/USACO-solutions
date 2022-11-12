// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <map>
using namespace std;

int main() {
	ifstream fin ("div7.in");
  	ofstream fout ("div7.out");
	int n; fin >> n;
	int psum[n+1];
	psum[0] = 0;
	for (int i = 0; i < n; i++) {
		int x; fin >> x;
		psum[i+1] = (x + psum[i]) % 7;
	}

	int ans = 0;
	map<int, int> found;
	for (int i = 1; i < n+1; i++) {
		int j = psum[i];
		if (found.count(j)==1) {
			int diff = i - found[j];
			ans = max(ans, diff);
		} else {
			found[j] = i;
		}
	}
	fout << ans << "\n";
}
