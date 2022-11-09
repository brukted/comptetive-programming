#include <bits/stdc++.h>
using namespace std;

#define send                              \
    {                                     \
        ios_base::sync_with_stdio(false); \
    }
#define help           \
    {                  \
        cin.tie(NULL); \
    }
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define inf 1e18
#define _size(v) ((int)v.size())
#define set_bits __builtin_popcountll
typedef long long ll;
typedef long double lld;
typedef unsigned long long ull;

template <typename A, typename B>
ostream &operator<<(ostream &cout, pair<A, B> const &p) { return cout << p.f << " " << p.s; }
template <typename A>
ostream &operator<<(ostream &cout, vector<A> const &v)
{
    for (int i = 0; i < v.size(); i++)
    {
        if (i)
            cout << " ";
        cout << v[i];
    }
    return cout << "";
}
template <typename A, typename B>
ostream &operator<<(ostream &cout, unordered_map<A, B> const &m)
{
    if (m.size() == 0)
        return cout << "{}";
    cout << "{";
    for (auto [k, v] : m)
    {
        cout << k << ": " << v << " , ";
    }
    return cout << "}";
}
template <typename A>
istream &operator>>(istream &cin, vector<A> &v)
{
    int i = 0;
    for (i = 0; i < _size(v) - 1; i++)
    {
        cin >> v[i];
    };
    return cin >> v[i];
}
template <typename A, typename B>
istream &operator>>(istream &cin, pair<A, B> &p)
{
    cin >> p.first;
    return cin >> p.second;
}

struct custom_hash
{
    static uint64_t splitmix64(uint64_t x)
    {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const
    {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

template <class t>
using vc = vector<t>;
template <class t>
using vvc = vc<vc<t>>;
template <class t>
using minheap = priority_queue<t, vc<t>, greater<t>>;
template <class t>
using maxheap = priority_queue<t>;

ll gcd(ll a, ll b)
{
    if (b > a)
    {
        return gcd(b, a);
    }
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
// mt19937 rng(61378913);
/* usage - just do rng() */

const lld pi = 3.14159265358979323846;
const ll mod = 1000000007;
// const ll mod = 998244353;
// ll mod;

void solve()
{
    int n;
    cin >> n;

    vc<set<int>> possibles(2 * n);

    for (auto i = 0; i < n; ++i)
    {
        for (auto j = n; j < 2 * n; ++j)
        {
            possibles[i].insert(j);
            possibles[j].insert(i);
        }
    }

    queue<pair<int, int>> que;
    que.push({0, n - 1});

    while (true)
    {
        int size = que.size();
        set<int> querySet;

        for (int j = 0; j < size; ++j)
        {
            auto [l, r] = que.front();
            que.pop();
            if (l == r)
                continue;

            auto mid = (l + r) / 2;

            for (auto i = l; i <= mid; ++i)
            {
                querySet.insert(i);
            }

            if (mid > l)
                que.push({l, mid});

            if (mid + 1 < r)
                que.push({mid + 1, r});
        }

        if (_size(querySet) == 0)
            break;

        cout << "ASK " << _size(querySet);
        for (auto i : querySet)
            cout << ' ' << i + 1;
        cout << '\n';
        cout.flush();

        set<int> ans;
        {
            int temp;
            for (auto i = 0; i < _size(querySet); ++i)
            {
                cin >> temp;
                ans.insert(temp - 1);
            }
        }

        for (auto i : querySet)
        {
            for (auto j = 0; j < n; ++j)
                if (!ans.count(j))
                    possibles[i].erase(j), possibles[j].erase(i);
        }

        for (auto j : ans)
        {
            for (auto i = 0; i < n; ++i)
            {
                if (!querySet.count(i))
                    possibles[i].erase(j), possibles[j].erase(i);
            }
        }
    }

    cout << "ANSWER";

    for (int i = n; i < 2 * n; i++)
        cout << " " << (*possibles[i].begin()) + 1;

    cout << endl;
}

int main()
{
    int tc = 1;
    // cin >> tc;
    for (int t = 0; t < tc; t++)
        solve();
}

/**

            else
            {
                for (auto j = 0; j < n; ++j)
                    if (isOn[j])
                        possibles[i][j] = false;
            }
 *
 */