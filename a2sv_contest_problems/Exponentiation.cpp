#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

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
        ll a, b;
        cin >> a >> b;
        cout << modExp(a, b, 1000000007) << '\n';
    }

    return 0;
}