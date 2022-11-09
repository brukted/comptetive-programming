#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <set>
#include <algorithm>
#include <functional>

#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<string> grid(n);
    for (auto &line : grid)
        cin >> line;

    vector<vector<int>> size(n, vector<int>(m, 1));
    vector<vector<pair<int, int>>> parent(n, vector<pair<int, int>>());

    for (auto i = 0; i < n; ++i)
        for (auto j = 0; j < m; ++j)
            parent[i].push_back({i, j});

    vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    function<pair<int, int>(pair<int, int>)> find = [&](pair<int, int> a) -> pair<int, int>
    {
        if (parent[a.first][a.second] == a)
            return a;

        auto p = find(parent[a.first][a.second]);
        parent[a.first][a.second] = p;
        return p;
    };

    auto unionF = [&](pair<int, int> a, pair<int, int> b) -> void
    {
        auto a_p = find(a);
        auto a_s = size[a_p.first][a_p.second];

        auto b_p = find(b);
        auto b_s = size[b_p.first][b_p.second];

        if (a_p == b_p)
            return;

        if (a_s < b_s)
        {
            swap(a_p, b_p);
            swap(a_s, b_s);
        }

        parent[b_p.first][b_p.second] = a_p;
        size[a_p.first][a_p.second] += b_s;
    };

    for (auto i = 0; i < n; ++i)
        for (auto j = 0; j < m; ++j)
        {
            if (grid[i][j] == '*')
                continue;

            for (auto [di, dj] : dirs)
            {
                int ni = i + di, nj = j + dj;
                if (0 <= ni and ni < n and 0 <= nj and nj < m and grid[ni][nj] == '.')
                {
                    unionF({i, j}, {ni, nj});
                }
            }
        }

    for (auto i = 0; i < n; ++i)
    {
        for (auto j = 0; j < m; ++j)
        {
            if (grid[i][j] == '.')
            {
                cout << '.';
                continue;
            }

            set<pair<int, int>> ss;
            int ans = 1;

            for (auto [di, dj] : dirs)
            {
                int ni = i + di, nj = j + dj;
                if (0 <= ni and ni < n and 0 <= nj and nj < m and grid[ni][nj] == '.')
                {
                    auto p = find({ni, nj});
                    if (!(ss.contains(p)))
                    {
                        ans += size[p.first][p.second];
                        ss.insert(p);
                    }
                }
            }

            cout << ans % 10;
        }
        cout << '\n';
    }

    return 0;
}