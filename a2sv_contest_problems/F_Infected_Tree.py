from collections import defaultdict
from functools import lru_cache
import sys
import threading


# BEGIN Template
from sys import stdin, stdout


def sng_int(): return int(stdin.readline())
def sng_str(): return stdin.readline()
def int_list(): return list(map(int, stdin.readline().split()))
def char_list(): return list(stdin.readline())
def spa_sep_str_list(): return list(stdin.readline().split())


def fst_print(*strings):
    for s in strings:
        stdout.write(s)
# End Template


def main():
    t = sng_int()

    edges = None
    sub_tree_size = None

    def make_tree(root):
        children = 0
        for child in edges[root]:
            edges[child].remove(root)
            children += make_tree(child)

        sub_tree_size[root] = children + 1
        return sub_tree_size[root]

    for _ in range(t):
        @lru_cache(None)
        def saved_count(infected_node):
            children = edges[infected_node]
            if len(children) == 1:
                return sub_tree_size[children[0]] - 1

            if len(children) == 0:
                return 0

            if len(children) == 2:
                l = saved_count(children[0])
                r = saved_count(children[1])
                a = max(l + sub_tree_size[children[1]] - 1,
                        r + sub_tree_size[children[0]] - 1)
                return a

        n = sng_int()
        edges = defaultdict(list)
        sub_tree_size = defaultdict(int)

        for _ in range(n-1):
            x, y = int_list()
            edges[x].append(y)
            edges[y].append(x)

        make_tree(1)

        best = saved_count(1)
        fst_print(str(best), '\n')
        saved_count.cache_clear()


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
