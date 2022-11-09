#include <iostream>
#include <math.h>

#define ll long long

using namespace std;

ll modExp(ll a, ll b, ll mod)
{
    if (b == 0)
        return 1;

    ll half = modExp(a, b >> 1, mod);

    if (b & 1)
    {
        half = (half * half) % mod;
        half = (half * a) % mod;
        return half;
    }

    return (half * half) % mod;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        ll i;
        ll m = 1e9 + 7;

        cin >> i;

        if (i <= 4)
            cout << i << '\n';
        else
        {
            ll ans;

            if (i % 3 == 2)
                ans = (modExp(3, i / 3, m) * 2) % m;
            else if (i % 3 == 1)
                ans = (modExp(3, (i - 4) / 3, m) * 4) % m;
            else
                ans = modExp(3, i / 3, m);
            
            cout << ans << '\n';
        }
    }

    return 0;
}