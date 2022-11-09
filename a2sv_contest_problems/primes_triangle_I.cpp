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

vector<pair<int, int>> ans(1e8 + 1);
vector<bool> is_prime(1e8 + 1, true);

void init()
{
    is_prime[0] = false;
    is_prime[1] = false;

    const auto limit = (ll)1e8 + 1;

    int row = 1;
    int row_count = 1;
    
    ans[2] = {1, 1};

    for (ll i = 3; i < limit; i += 2)
    {
        if (is_prime[i])
        {

            ++row_count;

            if (row_count > row)
            {
                row_count = 1;
                row += 1;
            }

            ans[i] = {row, row_count};
            if (i * i < limit)
                for (auto j = i * i; j < limit; j += i)
                    is_prime[j] = false;
        }
        else
            ans[i] = ans[i - 1];
    }
}

void solve()
{
    int n;
    cin >> n;
    if (is_prime[n] and n % 2)
        cout << ans[n].first << ' ' << ans[n].second << '\n';
    else
        cout << -1 << '\n';
}

int main()
{
    fast_io;

    init();

    int tc;
    cin >> tc;
    // cout << is_prime[3] << "##\n";
    for (auto i = 0; i < tc; ++i)
        solve();
}