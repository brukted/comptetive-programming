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
template<class t> using minheap=priority_queue<t, vc<t>, greater<t>>;
template<class t> using maxheap=priority_queue<t>;

// Math

ll gcd (ll a, ll b) { while (b) { a %= b; swap(a, b);} return a; }

ll bin_pow(ll a, ll b) { ll res = 1; while (b > 0) { if (b & 1) res = res * a; a = a * a;b >>= 1;} return res;}

const lld pi = 3.14159265358979323846;
const ll mod = 1e9 + 7;
// const ll mod = 998244353;
// ll mod;

// clang-format on

ll bin_pow(ll a, ll b, ll mod)
{
    ll res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = (res * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return res % mod;
}

void solve()
{
    ull n;
    cin >> n;
    ull sum = 0;
    ull i = 1;

    for (; i * i < n; ++i)
    {
        if (n % i == 0)
        {
            sum = (sum + i % mod) % mod;
            sum = (sum + (n / i) % mod) % mod;
        }
    }

    if (i * i == n)
        sum = (sum + i) % mod;

    cout << sum;
}

int main()
{
    fast_io;
    int tc;
    solve();
}