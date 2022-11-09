#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

using namespace std;

int main()
{
    const string hard = "hard";
    int n;
    cin >> n;
    string s;
    cin >> s;

    vector<long long> ambiguity(n);
    for (auto &x : ambiguity)
        cin >> x;

    vector<long long> dp(4);

    for (auto j = n - 1; j > -1; j -= 1)
    {
        for (auto i = 0; i < 4; i += 1)
        {
            if (i == 3)
            {
                if (hard[i] == s[j])
                    dp[i] = ambiguity[j] + dp[i];
                else
                    dp[i] = dp[i];
            }
            else if (hard[i] == s[j])
                dp[i] = min(ambiguity[j] + dp[i], dp[i + 1]);
            else
                dp[i] = dp[i];
        }
    }

    cout << dp[0] << "\n";
    return 0;
}