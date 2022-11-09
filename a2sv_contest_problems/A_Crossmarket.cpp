#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

void print() { cout << '\n'; }

template <typename T, typename... TAIL>
void print(const T &t, TAIL... tail)
{
    print(t);
    cout << ' ';
    print(tail...);
}

template <typename T>
void print(T x)
{
    cout << x;
}

int main()
{

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        int n, m;
        cin >> n >> m;

        if (n == 1 and m == 1)
            cout << 0 << '\n';
        else
            cout << min((2 * (m - 1)) + n, (2 * (n - 1)) + m) << '\n';
    }

    return 0;
}