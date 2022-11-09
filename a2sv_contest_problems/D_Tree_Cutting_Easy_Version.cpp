#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <map>
#include <functional>

#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> colors(n);
    int blue_count = 0;
    int reds_count = 0;

    for (auto &x : colors)
    {
        cin >> x;
        if (x == 2)
            blue_count += 1;
        else if (x == 1)
            ++reds_count;
    }

    map<int, vector<int>> tree;

    for (auto i = 0; i < n - 1; ++i)
    {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    int ans = 0;

    function<pair<int, int>(int, int)> dfs = [&](int node, int parent) -> pair<int, int>
    {
        int blues = 0;
        int reds = 0;

        for (auto child : tree[node])
        {
            if (child == parent)
                continue;
            auto [b, r] = dfs(child, node);
            blues += b;
            reds += r;
        }

        if (colors[node - 1] == 2)
            blues += 1;
        else if (colors[node - 1] == 1)
            reds += 1;

        if ((blues == blue_count and reds == 0) or (blues == 0 and reds == reds_count))
            ans += 1;
        // cout << node << ' ' << blues << endl;
        return {blues, reds};
    };

    dfs(1, -1);

    cout << ans << endl;
    return 0;
}