#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    cin.sync_with_stdio(false);

    int test_cases;
    cin >> test_cases;

    while (test_cases--)
    {
        int n;
        cin >> n;

        vector<long long> arr(n);
        for (auto &x : arr)
            cin >> x;

        if (n == 1)
        {
            cout << '0' << '\n';
            continue;
        }

        bool isSorted = true;

        for (int i = n - 2; i > -1; --i)
        {
            if (arr[i] > arr[i + 1])
            {
                isSorted = false;
                break;
            }
        }

        if (isSorted)
        {
            cout << "0\n";
            continue;
        }

        if (arr[n - 2] > arr[n - 1] or (arr[n - 2] < arr[n - 2] - arr[n - 1]))
        {
            cout << "-1" << '\n';
            continue;
        }

        cout << n - 2 << '\n';
        for (int i = n - 3; i > -1; --i)
        {
            cout << i + 1 << ' ' << n - 1 << ' ' << n << '\n';
        }
    }

    return 0;
}