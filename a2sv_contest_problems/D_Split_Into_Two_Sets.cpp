#include <iostream>
#include <set>
#include <map>
#include <vector>

using namespace std;

bool color(int node, int toColor, vector<int> &colors, map<int, set<int>> &graph)
{
    colors[node] = toColor;
    auto comClr = (toColor + 1) % 2;

    for (auto nei : graph[node])
    {
        if (colors[nei] == -1 && !color(nei, comClr, colors, graph))
        {
            return false;
        }
        else if (colors[nei] != comClr)
            return false;
    }

    return true;
}

int main()
{
    int t;
    cin >> t;
    int n;
    int a, b;
    auto graph = map<int, set<int>>();
    auto neighbors = map<int, set<int>>();
    bool can = true;
    auto colors = vector<int>();

    while (t--)
    {
        // reset
        cin >> n;
        graph.clear();
        neighbors.clear();
        colors.clear();
        can = true;

        for (int i = 0; i < n; ++i)
        {
            cin >> a >> b;

            if (a == b)
                can = false;

            if (can)
            {
                for (auto nei : neighbors[a])
                {
                    graph[i].insert(nei);
                    graph[nei].insert(i);
                }

                for (auto nei : neighbors[b])
                {
                    graph[i].insert(nei);
                    graph[nei].insert(i);
                }

                if (graph[i].size() > 2)
                    can = false;

                neighbors[a].insert(i);
                neighbors[b].insert(i);
            }
        }

        if (!can)
        {
            cout << "NO\n";
            continue;
        }

        colors.resize(n, -1);

        for (auto i = 0; i < n; ++i)
        {
            if (colors[i] == -1)
            {
                // cout << i << '\n';
                if (!color(i, 0, colors, graph))
                {
                    can = false;
                    break;
                }
            }
        }

        if (can)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}