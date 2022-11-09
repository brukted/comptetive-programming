#include <bits/stdc++.h>
using namespace std;

// clang-format off
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

template<typename A, typename B> ostream& operator<<(ostream &cout, pair<A, B> const &p) { return cout << p.f << " " << p.s; }
template<typename A> ostream& operator<<(ostream &cout, vector<A> const &v) {
    for(int i = 0; i < v.size(); i++) {if (i) cout << " "; cout << v[i];} return cout << "";
}

template<typename A> istream& operator>>(istream &cin, vector<A> &v) {
    int i=0; for(i = 0; i < _size(v)-1; i++) { cin >> v[i];}; return cin >> v[i];
}
template<typename A, typename B> istream& operator>>(istream& cin, pair<A, B> &p) {
    cin >> p.first;
    return cin >> p.second;
}

typedef long long ll;
typedef long double lld;
typedef unsigned long long ull;
// clang-format on

void solve()
{
    vector<ll> factorials(11, 1);
    for (ll i = 1; i <= 10; ++i)
        factorials[i] = factorials[i - 1] * i;

    auto nCr = [&](ll n, ll r)
    { return factorials[n] / (factorials[r] * factorials[n - r]); };

    // k success in n independent trials
    auto binomial = [&](ll k, ll n, double p)
    {
        return nCr(n, k) * pow(p, k) * pow(1.0 - p, n - k);
    };

    string intended;
    string received;
    cin >> intended >> received;
    int iP = 0, iM = 0, rP = 0, rM = 0, rU = 0, dP = 0;

    for (const auto ch : intended)
        if (ch == '+')
            ++iP;
        else
            ++iM;

    for (const auto ch : received)
        if (ch == '+')
            ++rP;
        else if (ch == '-')
            ++rM;

    rU = received.length() - rP - rM;
    dP = iP - rP;

    if (dP < 0 or dP > rU)
    {
        cout << setprecision(12) << fixed << 0.0 << endl;
        return;
    }

    cout << setprecision(12) << fixed << binomial(dP, rU, 0.5) << endl;
}

int main()
{
    fast_io;
    solve();
}