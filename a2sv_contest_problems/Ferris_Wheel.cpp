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

const lld pi = 3.14159265358979323846;
const ll mod = 1000000007;
// const ll mod = 998244353;
// ll mod;

// clang-format on

// 10 15
// 9 8 8 9 10 8 5 8 7 10

void solve()
{
    int n, x;
    cin >> n >> x;

    vector<int> arr(n);
    for (auto &i : arr) cin >> i;
    sort(arr.begin(), arr.end());

    int ans = 0, i = 0, j = n - 1;

    while (i <= j)
       if (arr[j] + arr[i] <= x)
            ++ans, ++i, --j;
        else
            ++ans, --j;

    cout << ans << endl;
}

int main()
{
    fast_io;
    solve();
}