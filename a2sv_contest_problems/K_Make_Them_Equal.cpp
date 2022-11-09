#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <unordered_map>

#define ll long long

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;
    unordered_map<ll, ll> memo;
    vector<ll> cost(1000 + 1, __LONG_LONG_MAX__);
    cost[1] = 0;

    for (auto target = 2LL; target <= 1000; ++target)
    {
        for (auto smaller_num = 1; smaller_num < target; ++smaller_num)
        {
            auto diff = target - smaller_num;
            if ((smaller_num / diff) == 0)
                continue;
            if (smaller_num / (smaller_num / diff) == diff)
                cost[target] = min(cost[target], 1 + cost[smaller_num]);
        }
    }

    for (int test = 0; test < test_cases; ++test)
    {

        ll n, k;
        cin >> n >> k;

        vector<ll> arr(n);
        for (auto &x : arr)
            cin >> x;

        vector<ll> coins(n);
        for (auto &x : coins)
            cin >> x;

        vector<ll> costs(n);
        for (auto i = 0; i < n; ++i)
            costs[i] = cost[arr[i]];

        vector<ll> dp_i_p_1(min(12 * n, k) + 1, 0);

        for (auto i = n - 1; i > -1; --i)
            for (auto budget = min(12 * n, k); budget > -1; --budget)
            {
                auto skip = dp_i_p_1[budget];
                auto dont_skip = 0LL;

                if (costs[i] <= budget)
                {
                    auto new_bud = budget - costs[i];
                    dont_skip += coins[i];

                    if (new_bud >= 0)
                        dont_skip += dp_i_p_1[new_bud];
                }

                dp_i_p_1[budget] = max(skip, dont_skip);
            }

        ll ans = 0;
        for (auto a : dp_i_p_1)
            ans = max(ans, a);

        std::cout << ans << '\n';
    }
    return 0;
}