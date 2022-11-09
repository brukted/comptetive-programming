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
// clang-format on

void solve()
{
    ull n;
    cin >> n;
    ull ans = 1;

    for (ull i = 0; i < 7; ++i)
        ans *= (n - i);
    ans /= 5040ULL;

    ull fives = 1;
    for (ull i = 0; i < 5; ++i)
        fives *= (n - i);
    fives /= 120ULL;

    ull sixes = 1;

    for (ull i = 0; i < 6; ++i)
        sixes *= (n - i);

    sixes /= 720ULL;

    cout << ans + fives + sixes << '\n';
}

int main()
{
    fast_io;
    solve();
}