#include <iostream>

#define ll long long

using namespace std;

ll modExp(ll a, ll b, ll mod)
{
    ll res = 1;

    while (b)
    {
        if (b & 1)
            res = (res * a) % mod;

        a = (a * a) % mod;
        b >>= 1;
    }

    return res % mod;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, k;

    while (cin >> n >> k)
    {
        if(n==0 && k==0) return 0;

        ll MOD = 1e7 + 7;
        ll ans = (2 * modExp(n - 1, k, MOD)) % MOD;
        ans = (ans + modExp(n, k, MOD)) % MOD;
        ans = (ans + (2 * modExp(n - 1, n - 1, MOD) % MOD)) % MOD;
        ans = (ans + modExp(n, n, MOD)) % MOD;

        cout << ans << '\n';
    }

    return 0;
}