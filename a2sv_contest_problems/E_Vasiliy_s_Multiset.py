from sys import stdin, stdout


class Node:
    def __init__(self) -> None:
        self.count = 0
        self.children = [None, None]


root = Node()
BITS = 31


def add(n: int):
    node = root
    node.count += 1

    for shift in range(BITS, -1, -1):
        idx = (n >> shift) & 1
        if node.children[idx] == None:
            node.children[idx] = Node()
        node = node.children[idx]
        node.count += 1


def remove(n, node=root, shift=BITS):
    node.count -= 1
    idx = (n >> shift) & 1
    curr = node.children[idx]

    if shift == 0:
        curr.count -= 1
        if curr.count == 0: node.children[idx] = None
        
        return curr.count == 0 and node.children[(idx + 1) % 2] == None

    res = remove(n, curr, shift - 1)
    
    if res:
        node.children[idx] = None

    return res and node.children[(idx + 1) % 2] == None


def ans(n):
    node = root
    res = 0

    for shift in range(BITS, -1, -1):
        nn = (((n >> shift) & 1) + 1) % 2

        if node.children[nn] != None and node.children[nn].count > 0:
            res |= 1 << shift
            node = node.children[nn]
        else:
            node = node.children[((n >> shift) & 1)]

    return res


t = int(stdin.readline().strip())

for i in range(t):
    op, n = stdin.readline().strip().split()
    n = int(n)

    add(0)

    if op == '+':
        add(n)
    elif op == '-':
        remove(n)
    else:
        print(ans(n))
