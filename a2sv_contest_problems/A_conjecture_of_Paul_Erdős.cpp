#include <bits/stdc++.h>
using namespace std;

// clang-format off

#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;
typedef long double lld;
typedef unsigned long long ull;

// clang-format on
vector<bool> is_prime;

void solve()
{
    ll limit;
    cin >> limit;
    limit += 1;

    vector<ll> perfect_squares;
    set<ll> perfect_quads;
    ll sqt = sqrt(limit);
    ll ssqt = sqrt(sqt);

    ll ans = 0;

    for (auto i = 2; i < limit; ++i)
    {
        if (i <= sqt)
            perfect_squares.emplace_back(i * i);
        if (i <= ssqt)
            perfect_quads.emplace(i * i * i * i);

        if (is_prime[i] and ((ll)i * i) < limit)
        {
            for (auto j = i * i; j < limit; j += i)
                is_prime[j] = false;
        }
    }

    cout << ans << '\n';
}

int main()
{
    is_prime[0] = false;
    is_prime[1] = false;
    
    fast_io;
    int tc;
    cin >> tc;
    for (auto i = 0; i < tc; ++i)
        solve();
}