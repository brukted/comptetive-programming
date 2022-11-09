#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <map>
#include <functional>

#define int long long

using namespace std;

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        map<int, vector<tuple<int, int, int>>> graph;

        int n;
        cin >> n;

        for (auto i = 1; i < n; ++i)
        {
            int p, a, b;
            cin >> p >> a >> b;

            graph[p].push_back({i + 1, a, b});
        }

        vector<int> ans(n + 1, 0);
        vector<int> bi_sum = {0};

        auto solve = [&](int a_sum) -> int
        {
            auto best = 0;
            int l = 0, r = bi_sum.size() - 1;

            while (l <= r)
            {
                int mid = (l + r) / 2;
                auto val = bi_sum[mid];
                if (val <= a_sum)
                {
                    best = mid;
                    l = mid + 1;
                }
                else
                    r = mid - 1;
            }

            return best;
        };

        function<void(int, int)> dfs = [&](int node, int a)
        {
            ans[node] = solve(a);

            for (auto [nei, aj, bj] : graph[node])
            {
                bi_sum.push_back(bi_sum[bi_sum.size() - 1] + bj);
                dfs(nei, a + aj);
                bi_sum.pop_back();
            }
        };

        dfs(1, 0);
        for (auto i = 2; i < ans.size(); ++i)
        {
            cout << ans[i] << (i != ans.size() - 1 ? ' ' : '\n');
        }
    }
}