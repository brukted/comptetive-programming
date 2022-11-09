#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <unordered_set>

#define ll long long

using namespace std;

struct pair_hash
{
    template <class T1, class T2>
    std::size_t operator()(const std::pair<T1, T2> &pair) const
    {
        return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, m, k;
    cin >> n >> m >> k;
    vector<int> satisfaction(n);
    for (auto &x : satisfaction)
        cin >> x;

    vector<vector<ll>> transition(n, vector<ll>(n, 0));
    for (auto i = 0; i < k; i++)
    {
        ll x, y, c;
        cin >> x >> y >> c;
        transition[x - 1][y - 1] = c;
    }

    unordered_set<pair<ll, ll>, pair_hash> visited;
    deque<tuple<ll, ll, ll, ll>> queue;

    for (auto i = 0; i < n; ++i)
    {
        visited.insert({1 << i, i});
        queue.push_back({1 << i, 1, i, 0});
    }

    ll ans = 0;
    while (queue.size())
    {
        auto [seen, count, curr, cumulative] = queue.front();
        queue.pop_front();

        if (count == m)
        {
        }
    }

    function<ll(ll, ll, ll)> solve = [&](ll seen, ll seen_count, ll curr) -> ll
    {
        if (memo.contains({seen, curr}))
            return memo[{seen, curr}];

        if (seen_count == m)
            return satisfaction[curr];

        ll ans = 0;

        for (auto next = 0; next < n; ++next)
        {
            if (seen & 1 << next)
                continue;

            ans = max(ans, solve(seen | 1 << next, seen_count + 1, next) + transition[curr][next]);
        }

        memo[{seen, curr}] = ans + satisfaction[curr];
        return ans + satisfaction[curr];
    };

    ll best = 0;

    for (auto i = 0; i < n; i++)
        best = max(best, solve(1 << i, 1, i));

    std::cout << best << endl;
    return 0;
}