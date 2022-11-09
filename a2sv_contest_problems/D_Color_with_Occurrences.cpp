#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

vector<int> rabin_karp(string const &s, string const &t)
{
    const int p = 31;
    const int m = 1e9 + 9;
    int S = s.size(), T = t.size();

    vector<long long> p_pow(max(S, T));
    p_pow[0] = 1;
    for (int i = 1; i < (int)p_pow.size(); i++)
        p_pow[i] = (p_pow[i - 1] * p) % m;

    vector<long long> h(T + 1, 0);
    for (int i = 0; i < T; i++)
        h[i + 1] = (h[i] + (t[i] - 'a' + 1) * p_pow[i]) % m;
    long long h_s = 0;
    for (int i = 0; i < S; i++)
        h_s = (h_s + (s[i] - 'a' + 1) * p_pow[i]) % m;

    vector<int> occurences;
    for (int i = 0; i + S - 1 < T; i++)
    {
        long long cur_h = (h[i + S] + m - h[i]) % m;
        if (cur_h == h_s * p_pow[i] % m)
            occurences.push_back(i);
    }
    return occurences;
}

int main()
{
    cin.sync_with_stdio(false);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        string t;
        cin >> t;

        int n;
        cin >> n;

        vector<tuple<int, int, int>> ranges;

        for (int i = 0; i < n; i++)
        {
            string s;
            cin >> s;

            vector<int> occs = rabin_karp(s, t);

            for (auto x : occs)
                ranges.emplace_back(x, x + s.size(), i + 1);
        }

        if (ranges.size() == 0)
        {
            cout << -1 << '\n';
            continue;
        }

        sort(ranges.begin(), ranges.end());

        int l_idx = 0;
        int r = 0;
        vector<tuple<int, int>> ans;

        // ans: string indx, start pos
        // ranges: start idx, end idx, string index

        while (l_idx < ranges.size() and r < t.size())
        {
            int r_max = 0;
            int r_max_idx = -1;

            while (l_idx < ranges.size() and get<0>(ranges[l_idx]) <= r)
            {
                if (get<1>(ranges[l_idx]) > r_max)
                {
                    r_max = get<1>(ranges[l_idx]);
                    r_max_idx = l_idx;
                }
                ++l_idx;
            }

            if (r == r_max)
                break;

            r = r_max;
            ans.emplace_back(get<0>(ranges[r_max_idx]), get<2>(ranges[r_max_idx]));
        }

        if (r == t.size())
        {
            cout << ans.size() << '\n';
            
            for (const auto i : ans)
                cout << get<1>(i) << ' ' << get<0>(i) + 1 << '\n';
        }
        else
            cout << -1 << '\n';
    }

    return 0;
}