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
    string data;
    cin >> data;
    double p;
    cin >> p;
    int unknowns = 0;
    int bad_days = 0;

    for (const auto d : data)
        if (d == '?')
            ++unknowns;
        else if (d == '1')
            ++bad_days;

    double ans = ((p * (double)unknowns) + (double)bad_days) / (double)data.size();
    printf("%0.5lf", ans);
}

int main()
{
    fast_io;
    solve();
}