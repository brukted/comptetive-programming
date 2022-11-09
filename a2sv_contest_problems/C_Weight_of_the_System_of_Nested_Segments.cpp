#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        string line;
        getline(cin, line);

        int n, m;
        cin >> n >> m;

        vector<tuple<int, int, int>> items;

        for (int i = 0; i < m; ++i)
        {
            int x, w;
            cin >> x >> w;
            items.emplace_back(x, w, i + 1);
        }

        // sort by weight
        sort(items.begin(), items.end(), [](auto const &t1, auto const &t2)
             { return get<1>(t1) < get<1>(t2); });

        // sort the first 2n points with the least weight by position
        sort(items.begin(), items.begin() + (2 * n));

        auto s = 0;

        for (int i = 0, end = 2 * n; i < end; ++i)
            s += get<1>(items[i]);

        cout << s << '\n';

        for (int i = 0, j = (2 * n) - 1; i < j; ++i, --j)
            cout << get<2>(items[i]) << ' ' << get<2>(items[j]) << '\n';

        cout << '\n';
    }

    return 0;
}