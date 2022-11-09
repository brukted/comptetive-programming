#include <bits/stdc++.h>
using namespace std;

// clang-format off

#define f first
#define s second
#define pb push_back
#define all(x) x.begin(), x.end()
#define inf 1e18
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;
typedef long double lld;
typedef unsigned long long ull;

// clang-format on

void solve()
{
    int n;
    cin >> n;
    int ans = 0;
    int i = 1;
    
    for (; i * i < n; ++i)
        if (n % i == 0)
            ++ans;

    ans *= 2;

    if (i * i == n)
        ++ans;

    cout << ans << '\n';
}

int main()
{
    fast_io;
    int tc;
    cin >> tc;
    for (auto i = 0; i < tc; ++i)
        solve();
}