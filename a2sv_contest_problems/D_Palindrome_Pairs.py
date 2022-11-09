from collections import Counter, defaultdict
from string import ascii_lowercase
from sys import stdin, stdout


class Node:
    def __init__(self, letter=chr(ord('a')-1)) -> None:
        self.count = 0
        self.letter = letter
        self.nodes = defaultdict(lambda: Node(chr(ord(letter)+1)))


n = int(stdin.readline().strip())
strs = []
for _ in range(n):
    strs.append(input())

root = Node()


def look(count, odd_encountered=False, node=root, shift=0):
    if node.count == 0:
        return 0

    if shift == 26:
        return node.count

    is_odd = count & (1 << shift)

    if is_odd:
        if odd_encountered:
            return look(count, odd_encountered, node.nodes[1], shift + 1)

        return look(count, False, node.nodes[1], shift + 1) + look(count, True, node.nodes[0], shift + 1)

    else:
        if odd_encountered:
            return look(count, odd_encountered, node.nodes[0], shift + 1)

        return look(count, True, node.nodes[1], shift + 1) + look(count, False, node.nodes[0], shift + 1)


def add(word):
    node = root
    count = Counter(word)
    for ch in ascii_lowercase:
        node.count += 1
        node = node.nodes[count[ch] % 2]
    node.count += 1


ans = 0

for word in strs:
    count = 0
    cc = Counter(word)

    for idx, ch in enumerate(ascii_lowercase):
        count |= cc[ch] % 2 << idx

    ans += look(count)
    add(word)

print(ans)
