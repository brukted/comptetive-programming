#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <map>
#include <algorithm>

using namespace std;

long long halfNotHalf(int i, int halves, long long k, const vector<long long> &arr, map<tuple<int, int>, long long> &memo)
{
    const auto stateKey = tuple<int, int>(i, halves);
    if (memo.contains(stateKey))
        return memo[stateKey];

    if (halves == 32 or i == arr.size())
        return 0;

    auto half = (arr[i] >> (halves + 1)) + halfNotHalf(i + 1, halves + 1, k, arr, memo);
    auto notHalf = (arr[i] >> (halves)) + halfNotHalf(i + 1, halves, k, arr, memo) - k;

    memo[stateKey] = max(half, notHalf);

    return memo[stateKey];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        int n;
        long long k;
        cin >> n >> k;

        vector<long long> arr(n);
        for (auto &x : arr)
            cin >> x;

        map<tuple<int, int>, long long> memo;
        cout << halfNotHalf(0, 0, k, arr, memo) << '\n';
    }

    return 0;
}