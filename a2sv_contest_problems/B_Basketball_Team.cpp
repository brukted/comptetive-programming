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
    int n, m, h;
    cin >> n >> m >> h;

    int totalPlayers = 0;
    vector<int> s(m);

    for (auto &x : s)
    {
        cin >> x;
        totalPlayers += x;
    }

    if (totalPlayers < n)
    {
        cout << -1 << '\n';
        return;
    }

    totalPlayers -= s[h - 1];
    s[h - 1] -= 1;
    lld ans = 1.0;

    for (auto i = 0; i < n - 1; ++i)
    {
        ans *= ((float)totalPlayers / ((float)totalPlayers + s[h - 1]));
        
        if (totalPlayers != 0)
            totalPlayers -= 1;
    }

    cout << 1.0 - ans << '\n';
}

int main()
{
    fast_io;
    solve();
}