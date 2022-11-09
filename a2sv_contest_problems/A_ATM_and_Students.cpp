#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

void main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        int n;
        long long s;
        cin >> n >> s;

        std::vector<long long> arr;
        std::vector<long long> prefix;
        prefix.reserve(n);
        arr.reserve(n);

        long long number;

        while (cin >> number)
        {
            arr.push_back(number);
        }

        int start = 0;
        int end = -2;

        for (int i = 0; i < n; ++i)
        {
            long long ss = s;
            int j = i;

            while (j < i && arr[j] + ss >= 0)
            {
                ss += arr[j];
                j += 1;
            }
        }
    }
}