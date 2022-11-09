#include <string>
#include <vector>
#include <iostream>
#include <deque>
#include <tuple>
#include <algorithm>

#define ll long long

using namespace std;

struct Node
{
    int count = 0;
    Node *children[2] = {nullptr, nullptr};
};

int BITS = 31;

int ans(int n, Node *node)
{
    auto res = 0;

    for (auto shift = BITS; shift > -1; --shift)
    {
        auto nn = (((n >> shift) & 1) + 1) % 2;

        if (node->children[nn] != nullptr and node->children[nn]->count > 0)
        {
            res |= 1 << shift;
            node = node->children[nn];
        }
        else
            node = node->children[((n >> shift) & 1)];
    }

    return res;
}

bool remove(int n, Node *node, int shift = BITS)
{
    --node->count;
    auto idx = (n >> shift) & 1;
    auto curr = node->children[idx];

    if (shift == 0)
    {
        --curr->count;
        if (curr->count == 0)
            node->children[idx] = nullptr;

        return curr->count == 0 and node->children[(idx + 1) % 2] == nullptr;
    }

    auto res = remove(n, curr, shift - 1);

    if (res)
    {
        delete node->children[idx];
        node->children[idx] = nullptr;
    }

    return res and node->children[(idx + 1) % 2] == nullptr;
}

void add(Node *node, int n)
{
    ++node->count;

    for (auto shift = BITS; shift > -1; --shift)
    {
        auto idx = (n >> shift) & 1;
        if (node->children[idx] == nullptr)
            node->children[idx] = new Node();

        node = node->children[idx];
        ++node->count;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Node *root = new Node();

    add(root, 0);

    int test_cases;
    cin >> test_cases;

    for (int test = 0; test < test_cases; ++test)
    {
        char op;
        int n;
        cin >> op >> n;
        if (op == '+')
            add(root, n);
        else if (op == '-')
            remove(n, root);
        else
            cout << ans(n, root) << '\n';
    }

    return 0;
}