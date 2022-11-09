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

    int n;
    cin >> n;
    vector<int> arr(n);
    for (auto &x : arr)
        cin >> x;

    int n_2 = 0;
    int n_1 = 1;
    int ans = 0;
    for (int i = n - 2; i > -1; --i)
    {
        ans = max(n_2, n_1);
        int curr = 0;
        if(arr[i + 1] > arr[i])
            curr = max(curr, n_1 + 1);
        else if(arr[i + 2] > arr[i])
            curr =  max(curr, n_2 + 1;
        
        n_2 = n_1;
        
    }

    ans = max(n_2, n_1);
    cout << ans << '\n';
    return 0;
}