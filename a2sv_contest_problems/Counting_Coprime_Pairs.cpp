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

vector<bool> is_prime(1e6 + 5, true);

void init()
{
    is_prime[0] = false;
    is_prime[1] = false;

    const auto limit = (ll)1e6 + 5;

    for (ll i = 2; i < limit; ++i)
    {
        if (is_prime[i])
        {
            // Normal sieve
            for (auto j = i * i; j < limit; j += i)
                is_prime[j] = false;

            string num_str = to_string(i);
            bool fearFul = true;

            for (auto k = 1; k < num_str.size(); ++k)
            {
                if (not is_prime[stoi(num_str.substr(k))] or num_str[k] == '0')
                {
                    fearFul = false;
                    break;
                }
            }

            if (fearFul)
                ans[i] = ans[i - 1] + 1;
            else
                ans[i] = ans[i - 1];
        }
        else
            ans[i] = ans[i - 1];
    }
}

void solve()
{
    int n;
    cin >> n;
    cout << ans[n] << '\n';
}

int main()
{
    fast_io;
    init();
    int tc;
    cin >> tc;
    for (auto i = 0; i < tc; ++i)
        solve();
}