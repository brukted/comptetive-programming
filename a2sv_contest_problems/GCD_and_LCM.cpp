#include <iostream>

#define ll long long

using namespace std;

int gcd(ll a, ll b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main()
{

    int t;
    cin >> t;

    for (auto i = 0; i < t; ++i)
    {
        ll a, b;

        cin >> a >> b;

        if (a > b)
        {
            ll _gcd = gcd(a, b);
            cout << _gcd << ' ' << (a / _gcd) * b << '\n';
        }
        else
        {
            ll _gcd = gcd(b, a);
            cout << _gcd << ' ' << (a / _gcd) * b << '\n';
        }
    }
    return 0;
}
