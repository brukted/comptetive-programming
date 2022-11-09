#include <iostream>
#include <map>
#include <vector>

using namespace std;

int make_tree(int root, map<int, vector<int>> edges, map<int, int> sub_tree_size)
{
    int children = 0;
    for (const int child : edges[root])
    {
        auto it = std::remove(edges[root].begin(), edges[root].end(), root);
        edges[root].erase(it);
        children += make_tree(child, edges, sub_tree_size);
    }
    sub_tree_size[root] = children + 1;
    return children + 1;
}

int saved_count(int infected_node, map<int, vector<int>> edges, map<int, int> sub_tree_size, map<int, int> memo)
{
    if (memo.find(infected_node) != memo.end())
        return memo[infected_node];
    vector<int> children = edges[infected_node];

    if (children.size() == 1)
        return sub_tree_size[children[0]] - 1;

    else if (children.size() == 0)
        return 0;
    else
    {
        int l = saved_count(children[0], edges, sub_tree_size, memo);
        int r = saved_count(children[1], edges, sub_tree_size, memo);
        return max(l + sub_tree_size[children[1]] - 1, r + sub_tree_size[children[0]] - 1);
    }
}

int main()
{
    int t = 0;
    cin >> t;

    while (t > 0)
    {
        int n = 0;
        cin >> n;
        map<int, vector<int>> edges;
        map<int, int> sub_tree_size;
        map<int, int> memo;

        for (int i = 0; i < n; ++i)
        {
            int x, y;
            cin >> x >> y;
            edges[x].push_back(y);
            edges[y].push_back(x);
        }

        make_tree(1, edges, sub_tree_size);
        int ans = saved_count(1, edges, sub_tree_size, memo);
        cout << ans << endl;
        --t;
    }
}