#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

#define ll long long

using namespace std;

ll gcd(ll a, ll b)
{
    while (b)
    {
        a %= b;
        swap(a, b);
    }
    return a;
}

ll gcd_extended(ll a, ll b, ll &x, ll &y)
{
    if (b == 0)
    {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1;
    ll d = gcd_extended(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

bool find_any_solution(ll a, ll b, ll c, ll &x0, ll &y0, ll &g)
{
    g = gcd_extended(abs(a), abs(b), x0, y0);
    if (c % g)
    {
        return false;
    }

    x0 *= c / g;
    y0 *= c / g;
    if (a < 0)
        x0 = -x0;
    if (b < 0)
        y0 = -y0;
    return true;
}

pair<ll, ll> solve(ll a, ll b, ll c, ll d)
{
    pair<ll, ll> ans = {-1LL, -1LL};

    ll m = a * b;

    for (ll x = a + 1; x <= c; ++x)
    {
        ll k, y, g;
        find_any_solution(x, m, 0, y, k, g);

        auto bog = m / g;

        while (y <= d)
        {
            if (y > b and y <= d)
            {
                ans = {x, y};
                break;
            }
            y += bog;
        }
    }

    return ans;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        pair<ll, ll> ans = solve(a, b, c, d);
        cout << ans.first << ' ' << ans.second << '\n';
    }

    return 0;
}