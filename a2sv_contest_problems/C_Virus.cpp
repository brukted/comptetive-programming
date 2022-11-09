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
#define for_i(end) for (auto i = 0; i < end; ++i)
#define forr_i(start) for (auto i = start; i > -1; --i)
#define for_se(start, end) for (auto i = start; i < end; ++i)
#define forr_se(start, end) for (auto i = start; i > end; --i)
#define lIdx(vec) vec.size() - 1
#define sz(vec) vec.size()

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

const lld pi = 3.14159265358979323846;
const ll mod = 1000000007;
// const ll mod = 998244353;
// ll mod;

// clang-format on

void solve()
{
    int n, m, temp, ans = 0;
    vc<int> segments;

    cin >> n >> m;

    vector<int> infected(m);
    for (auto &x : infected)
        cin >> x;

    sort(infected.begin(), infected.end());

    int last = 0;
    for_i(m)
    {
        if (segments.size() == 0 or (infected[i] - last - 1) > 0)
            segments.push_back(infected[i] - last - 1);
        last = infected[i];
    }

    segments[0] += n - infected[lIdx(infected)];

    sort(segments.begin(), segments.end(), greater<int>());

    int pro = 0;

    for_i(sz(segments))
    {
        int sz = segments[i] - (pro * 4);
        if (sz > 1)
            ans += sz - 1;
        else if (sz == 1)
            ans += sz;
        else
            break;
        ++pro;
    }

    cout << n - ans << endl;
}

int main()
{
    fast_io;
    int tc;
    cin >> tc;

    for_i(tc)
        solve();
}