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

map<tuple<int, int, int>, bool> memo;

bool canAlexAlwaysWin(int remain, int turn = 1, bool isAlex = true)
{
    auto stateKey = tuple<int, int, int>(remain, turn, isAlex);

    if (memo.find(stateKey) != memo.end())
        return memo[stateKey];

    bool ans = false;

    if (remain == 0) // Hope not alex
        ans = !isAlex;

    else if (isAlex)
    {
        ans = false;

        // Can win by choosing one of them
        for (auto i = 1, end = min(turn, remain); i <= end; ++i)
        {
            if (canAlexAlwaysWin(remain - i, turn + 1, !isAlex))
            {
                ans = true;
                break;
            }
        }
    }

    else
    {
        ans = true;
        for (auto i = 1, end = min(turn, remain); i <= end; ++i)
            if (!canAlexAlwaysWin(remain - i, turn + 1, !isAlex))
            {
                ans = false;
                break;
            }
    }

    memo[stateKey] = ans;
    return ans;
}

void solve()
{
    int n;
    cin >> n;
    
    if (canAlexAlwaysWin(n))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

int main()
{
    fast_io;
    solve();
}