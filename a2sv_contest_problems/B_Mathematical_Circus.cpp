#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

int main()
{
    cin.sync_with_stdio(false);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        int n, k;
        cin >> n >> k;

        if (k % 4 == 0)
        {
            cout << "NO\n";
            continue;
        }

        cout << "YES\n";

        if (k % 2 == 1)
        {
            for (int i = 1; i < n; i += 2)
            {
                cout << i << " " << i + 1 << '\n';
            }
        }
        else
        {
            for (int i = 1; i < n; i += 2)
            {
                if ((i + 1) % 4 == 0)
                    cout << i << " " << i + 1 << '\n';
                else
                    cout << i + 1 << " " << i << '\n';
            }
        }
    }

    return 0;
}