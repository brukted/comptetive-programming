#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

int josephus(int n, int j, int k = 2)
{
    int res = 0;
    for (int i = 1; i <= n; ++i)
        res = (res + k) % i;
    return res + 1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        int n, k;
        cin >> n >> k;
        cout << josephus(n, k + 3) << '\n';
    }

    return 0;
}