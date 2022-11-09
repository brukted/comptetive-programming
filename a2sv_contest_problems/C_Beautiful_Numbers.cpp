#include <bits/stdc++.h>
using namespace std;

// clang-format off

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define inf 1e18
#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;
typedef long double lld;
typedef unsigned long long ull;

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

template<class t> using vc=vector<t>;
// Math
ll modExp(ll a, ll b, ll mod){ if (b == 0) return 1;    ll half = modExp(a, b >> 1, mod);   if (b & 1){ half = (half * half) % mod; half = (half * a) % mod;    return half;}   return (half * half) % mod;}

const lld pi = 3.14159265358979323846;
const ll mod = 1e9 +7;

// clang-format on

vc<ll> factorials;
vc<ll> factorialsInverse;

void initFactorials(ll n)
{
    factorials = vc<ll>(n + 1);
    factorialsInverse = vc<ll>(n + 1);

    factorials[0] = 1;

    for (ll i = 1; i <= n; ++i)
        factorials[i] = (factorials[i - 1] * i) % mod;

    for (ll i = 0; i <= n; ++i)
        factorialsInverse[i] = modExp(factorials[i], mod - 2, mod);
}

bool isGood(ll a, ll b, ll x)
{
    while (x > 0LL)
    {
        if (x % 10LL != a and x % 10LL != b)
            return false;
        x /= 10;
    }
    return true;
}

void solve()
{
    ll a, b, n;
    cin >> a >> b >> n;

    if (a == b)
    {
        if (isGood(a, a, a * n))
            cout << 1 << '\n';
        else
            cout << 0 << '\n';
        return;
    }

    initFactorials(n);
    ll ans = 0;

    for (ll i = 0; i <= n; ++i)
    {
        if (isGood(a, b, i * a + (n - i) * b))
        {
            ans += ((factorials[n] * factorialsInverse[i]) % mod * factorialsInverse[n - i]) % mod;
            ans %= mod;
        }
    }

    cout << ans << '\n';
}

int main()
{
    fast_io;
    solve();
    return 0;
}
