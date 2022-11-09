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

    int a, x, y;
    cin >> a >> x >> y;

    if (x > 0 and x < a and y > 0 and y < a)
        cout << 0 << '\n';
    else if (x < 0 or x > a or y < 0 or y > a)
        cout << 2 << '\n';
    else
        cout << 1 << '\n';

    return 0;
}