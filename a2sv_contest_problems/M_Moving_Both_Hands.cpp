#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>

#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, m;
    cin >> n >> m;

    map<ll, vector<pair<ll, ll>>> graph;
    // reversed graph
    map<ll, vector<pair<ll, ll>>> r_graph;

    vector<vector<ll>> best(2, vector<ll>(n + 1, __LONG_LONG_MAX__));

    best[0][1] = 0;
    best[1][1] = 0;

    for (auto i = 0; i < m; ++i)
    {
        ll u, v, w;
        cin >> u >> v >> w;

        graph[u].push_back({v, w});
        r_graph[v].push_back({u, w});
    }

    priority_queue<tuple<ll, ll, ll>> heap;
    heap.push({0, 1, 0});

    while (!heap.empty())
    {
        auto [distance, node, direction] = heap.top();
        distance *= -1;
        heap.pop();

        if (distance > best[direction][node])
            continue;

        if (direction == 0)
        {

            for (auto [nei, w] : graph[node])
            {
                if (w + distance < best[0][nei])
                {
                    heap.push({-1 * (w + distance), nei, 0});
                    best[0][nei] = w + distance;
                }
            }
        }

        for (auto [nei, w] : r_graph[node])
        {
            if (w + distance < best[1][nei])
            {
                heap.push({-1 * (w + distance), nei, 1});
                best[1][nei] = w + distance;
            }
        }
    }

    for (auto i = 2; i <= n; ++i)
    {
        auto ans = min(best[0][i], best[1][i]);
        if (ans == __LONG_LONG_MAX__)
            ans = -1;
        cout << ans << (i != n ? ' ' : '\n');
    }

    return 0;
}