#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;
    vector<vector<long long>> min_path(n, vector<long long>(n));

    for (auto &row : min_path)
        for (auto &cell : row)
            cin >> cell;

    vector<long long> order(n);
    for (auto &x : order)
    {
        cin >> x;
        --x;
    }

    reverse(order.begin(), order.end());

    vector<long long> ans;
    long long curr = 0;
    vector<vector<bool>> ss(n, vector<bool>(n, false));
    vector<bool> graph_nodes(n, false);

    for (auto k : order)
    {
        graph_nodes[k] = true;

        for (auto i = 0; i < n; ++i)
        {
            for (auto j = 0; j < n; ++j)
            {
                auto i_j_old = min_path[i][j];
                auto j_i_old = min_path[j][i];

                if (min_path[i][k] + min_path[k][j] < min_path[i][j])
                    min_path[i][j] = min_path[i][k] + min_path[k][j];

                if (min_path[j][k] + min_path[k][i] < min_path[j][i])
                    min_path[j][i] = min_path[k][i] + min_path[j][k];

                if (graph_nodes[i] and graph_nodes[j])
                {
                    if (ss[i][j])
                        curr -= i_j_old;
                    if (ss[j][i])
                        curr -= j_i_old;

                    ss[i][j] = true;
                    curr += min_path[i][j];

                    ss[j][i] = true;
                    curr += min_path[j][i];
                }
            }
        }

        ans.push_back(curr);
    }

    reverse(ans.begin(), ans.end());

    for (auto i = 0; i < ans.size(); ++i)
    {
        cout << ans[i] << (i == ans.size() - 1 ? '\n' : ' ');
    }

    return 0;
}