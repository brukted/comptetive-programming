#include <bits/stdc++.h>
using namespace std;

// clang-format off

#define f first
#define s second
#define pb push_back
#define all(x) x.begin(), x.end()
#define inf 1e18
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

ll solve()
{
    ll n;
    cin >> n;
    vector<ll> arr(2 * n);

    for (auto &x : arr)
        cin >> x;

    reverse(arr.begin(), arr.end());

    stack<ll> s;

    for (auto i : arr)
        if (s.size() == 0)
        {
            s.push(i);
            continue;
        }

        else if (s.top() == i)
            s.pop();
        else

            s.push(i);

    if (s.size() != 0)
        return -1;
    else
        return 2 * n;
}

int main()
{
    fast_io;
    ll ans = solve();

    if (ans == -1)
        cout << "impossible" << endl;
    else
        cout << ans << endl;
}