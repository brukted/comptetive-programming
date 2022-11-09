#include <cstdio>
#include <cstring>
using namespace std;
typedef long long ll;

const int N = 1e5 + 5, MOD = 1e9 + 7;
char str[N];
ll dp[N];

int main() {
	int n;
	scanf("%s", str + 1);
	n = strlen(str + 1);
	dp[1] = 1;
	dp[2] = 2;

	for (int i = 3; i <= n; i++) {
		dp[i] = (dp[i] + dp[i - 1] + dp[i - 2]) % MOD;
	}

	ll ans = 1;

	for (int i = 1; i <= n; i++) {
		if (str[i] == 'm' || str[i] == 'w') {
			printf("0");
			return 0;
		} else if (str[i] == 'u' || str[i] == 'n') {
			int j = i;
			while (j <= n && str[j] == str[i]) j++; 
			ans = (ans * dp[j - i]) % MOD;
			i = j - 1;//注意要跳到下一个字符上 
		}
	}
	printf("%lld", ans);
	return 0;
}