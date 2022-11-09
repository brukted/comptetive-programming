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
    ull a, b;
    cin >> a >> b;

    vector<ull> subGamesRounds;

    if (a > b)
        swap(a, b);

    while (a != 0 and b != 0)
    {
        subGamesRounds.push_back(b / a);

        b = b % a;
        swap(a, b);
    }

    function<bool(size_t, bool)> canAlwaysWin = [&](size_t subGame, bool isMe)
    {
        if (subGame == subGamesRounds.size() - 1)
            return isMe;

        if (subGamesRounds[subGame] == 1)
            return canAlwaysWin(subGame + 1, !isMe);

        if (isMe)
            return canAlwaysWin(subGame + 1, isMe) or canAlwaysWin(subGame + 1, !isMe);
        else
            return canAlwaysWin(subGame + 1, isMe) and canAlwaysWin(subGame + 1, !isMe);
    };

    if (canAlwaysWin(0, true))
        cout << "win" << endl;
    else
        cout << "lose" << endl;
}

int main()
{
    fast_io;
    solve();
}