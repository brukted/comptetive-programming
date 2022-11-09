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

void solve()
{
    int n, m;
    cin >> n >> m;
    map<int, set<int>> indegree;

    for (int i = 1; i <= n; ++i)
        indegree[i] = set<int>();

    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        indegree[a].insert(b);
        indegree[b].insert(a);
    }

    for (int i = 1; i <= n; ++i)
    {
        if (i != 1)
            cout << ' ';
        cout << (int)indegree[i].size() - i;
    }

    cout << endl;
}

int main()
{
    fast_io;
    solve();
}