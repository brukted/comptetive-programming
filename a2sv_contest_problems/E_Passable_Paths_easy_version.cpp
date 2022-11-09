#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int u, v;

    map<int, vector<int>> graph;

    while (--n)
    {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int q;
    cin >> q;

    int k;
    int temp;
    set<int> query;

    while (--q)
    {
        cin >> k;
        query.clear();
        while (--k)
        {
            cin >> temp;
            query.insert(temp);
        }
    }

    return 0;
}