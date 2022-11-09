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

    int n, m;
    cin >> n >> m;

    vector<ll> arr(n);

    for (auto &x : arr)
        cin >> x;

    vector<ll> left_to_right(n, 0);

    for (ll i = 1, prefix = 0; i < n; ++i)
    {
        if (arr[i - 1] > arr[i])
            prefix += arr[i - 1] - arr[i];
        left_to_right[i] = prefix;
    }

    vector<ll> right_to_left(n, 0);

    for (ll i = n - 2, postfix = 0; i > -1; --i)
    {
        if (arr[i + 1] > arr[i])
            postfix += arr[i + 1] - arr[i];
        right_to_left[i] = postfix;
    }

    for (auto i = 0; i < m; ++i)
    {
        int s, t;
        cin >> s >> t;

        if (s < t)
            cout << left_to_right[t - 1] - left_to_right[s - 1] << '\n';
        else
            cout << right_to_left[t - 1] - right_to_left[s - 1] << '\n';
    }

    return 0;
}