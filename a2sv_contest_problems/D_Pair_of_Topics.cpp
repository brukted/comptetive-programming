#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

int binary_search(vector<int> &arr, int val, int l, int r)
{
    int best = -1;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] >= val)
        {
            best = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }

    return best;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);
    for (auto &x : a)
        cin >> x;

    vector<int> c(n);

    for (auto i = 0; i < n; ++i)
    {
        int b;
        cin >> b;
        c[i] = a[i] - b;
    }

    sort(c.begin(), c.end());

    long long topics = 0;

    for (auto i = 0; i < n; i++)
    {
        auto idx = binary_search(c, -c[i] + 1, 0, i - 1);

        if (idx != -1)
            topics += i - idx;
    }

    cout << topics << "\n";

    return 0;
}