#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <map>

using namespace std;

tuple<vector<int>, int> solve(const int root, const int parent, const int k, vector<vector<int>> &tree)
{
    auto depth_count = vector<int>(k);
    depth_count[0] = 1;

    if (tree[root].empty())
        return {depth_count, 0};

    auto cumulative_answer = 0;

    for (const auto child : tree[root])
    {
        if (child == parent)
            continue;

        const auto [child_depth_counts, child_answer] = solve(child, root, k, tree);
        cumulative_answer += child_answer;

        for (auto i = 0; i < k; ++i)
            cumulative_answer += child_depth_counts[i] * depth_count[k - 1 - i];

        for (auto i = 0; i < k - 1; ++i)
            depth_count[i + 1] += child_depth_counts[i];
    }

    return {depth_count, cumulative_answer};
}

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    auto tree = vector<vector<int>>(n);

    int u, v;

    for (int i = 0; i < n - 1; ++i)
    {
        cin >> u >> v;
        --u;
        --v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    const auto [depth_counts, answer] = solve(0, -1, k, tree);

    cout << answer << '\n';

    return 0;
}