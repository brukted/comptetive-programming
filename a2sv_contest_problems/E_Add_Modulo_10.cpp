#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <cmath>

#define ll long long

using namespace std;

int group(long a)
{
    if (a % 3 == 0 or a == 7)
        return 0;
    else
        return 1;
}

int main()
{
    cin.sync_with_stdio(false);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        int n;
        cin >> n;

        long base;
        long parity;
        long mod;
        long mod_parity;
        bool can = true;

        long a;

        cin >> a;

        mod = a % 10;
        mod_parity = group(mod);
        base = a;
        parity = (a / 10) % 2;
        n -= 1;

        while (n-- != 0)
        {
            cin >> a;
            if (mod == 0 or mod == 5)
                can &= ((a + (a % 10)) == base) or a == base or (base + base % 10) == a;

            else
            {
                can &= a % 5 != 0;

                if (a % 10 == 1)
                    a += 1;
                can &= ((group(a % 10) == mod_parity) and (a / 10) % 2 == parity) or ((group(a % 10) != mod_parity) and (a / 10) % 2 != parity);
            }
            // cout << a << ' ' << can << '\n';
        }

        // cout << "###\n";

        if (can)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
}