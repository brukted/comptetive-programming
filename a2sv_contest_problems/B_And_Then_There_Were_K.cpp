#include <iostream>
#include <cmath>

using namespace std;

int main()
{

    int tests;
    cin >> tests;

    for (; tests > 0; --tests)
    {
        unsigned long n1 = 0;
        unsigned long n = 0;
        cin >> n1;

        n = n1;

        unsigned int largest = 0;

        while (n != 0)
        {
            n >>= 1;
            ++largest;
        }

        unsigned long ans = (1 << (largest - 1)) - 1;

        cout << ans <<"\n";
    }
}