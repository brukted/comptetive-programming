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

struct Dice
{
    int matrix[4][4];

    Dice()
    {
        for (auto i = 0; i < 4; ++i)
            for (auto j = 0; j < 4; ++j)
                matrix[i][j] = 0;

        matrix[0][1] = 4;
        matrix[1][0] = 5, matrix[1][1] = 1, matrix[1][2] = 2, matrix[1][3] = 6;
        matrix[2][1] = 3;
    }

    void moveUp()
    {
        int prev = matrix[2][1];

        int temp = matrix[1][1];
        matrix[1][1] = prev;
        prev = temp;

        temp = matrix[0][1];
        matrix[0][1] = prev;
        prev = temp;

        temp = matrix[1][3];
        matrix[1][3] = prev;
        prev = temp;

        temp = matrix[2][1];
        matrix[2][1] = prev;
        prev = temp;
    }

    void moveDown()
    {
        int prev = matrix[1][1];

        int temp = matrix[2][1];
        matrix[2][1] = prev;
        prev = temp;

        temp = matrix[1][3];
        matrix[1][3] = prev;
        prev = temp;

        temp = matrix[0][1];
        matrix[0][1] = prev;
        prev = temp;

        temp = matrix[1][1];
        matrix[1][1] = prev;
        prev = temp;
    }

    void moveRight()
    {
        int prev = matrix[1][0];

        for (auto i = 1; i <= 4; ++i)
        {
            int temp = matrix[1][i % 4];
            matrix[1][i % 4] = prev;
            prev = temp;
        }
    }

    void moveLeft()
    {
        int prev = matrix[1][3];

        for (auto i = 6; i > 2; --i)
        {
            int temp = matrix[1][i % 4];
            matrix[1][i % 4] = prev;
            prev = temp;
        }
    }
};

void solve()
{
    int n;
    cin >> n;

    vector<string> grid(n);
    for (auto &x : grid)
        cin >> x;

    int si, sj;
    int gi, gj;

    for (auto i = 0; i < n; ++i)
        for (auto j = 0; j < n; ++j)
            if (grid[i][j] == 'S')
                si = i, sj = j;
            else if (grid[i][j] == 'H')
                gi = i, gj = j;

    auto isInbound = [&](int i, int j)
    {
        return 0 <= i and i < n and 0 <= j and j < n;
    };

    // l, u, d , r
    vector<pair<int, int>> dirs = {
        {0, -1},
        {-1, 0},
        {1, 0},
        {0, 1},
    };

    unordered_set<ll> seen;

    function<bool(int, int, Dice)> dfs = [&](int i, int j, Dice d)
    {
        if (i == gi and j == gj and d.matrix[1][3] == 5)
            return true;

        for (auto k = 0; k < 4; ++k)
        {
            auto [di, dj] = dirs[k];

            if (isInbound(i + di, j + dj) and grid[i + di][j + dj] != '*')
            {
                Dice dd = d;

                switch (k)
                {
                case 0:
                    dd.moveLeft();
                    break;
                case 1:
                    dd.moveUp();
                    break;
                case 2:
                    dd.moveDown();
                    break;
                case 3:
                    dd.moveRight();
                    break;
                }

                auto key = (((((ll)(i + di) * 100LL) + (ll)(j + dj)) * 10LL + (ll)dd.matrix[1][1]) * 10LL) + (ll)dd.matrix[2][1];

                if (seen.find(key) != seen.end())
                    continue;

                seen.insert(key);

                if (dfs(i + di, j + dj, dd))
                    return true;
            }
        }

        return false;
    };

    Dice d;
    auto key = (((((ll)(si)*100LL) + (ll)(sj)) * 10LL + (ll)d.matrix[1][1]) * 10LL) + (ll)d.matrix[2][1];
    seen.insert(key);

    if (dfs(si, sj, d))
        cout << "Yes\n";
    else
        cout << "No\n";
}

int main()
{
    fast_io;

    int tc;
    cin >> tc;
    for (auto i = 0; i < tc; ++i)
        solve();
}