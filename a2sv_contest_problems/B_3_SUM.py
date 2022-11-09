from functools import lru_cache
from sys import stdin, stdout
import threading
import sys
from typing import Counter


def main():
    t = int(stdin.readline().strip())

    for _ in range(t):
        n = int(stdin.readline().strip())
        arr = list(map(int, stdin.readline().split()))
        arr = Counter(map(lambda x: x % 10, arr))
        two_sums = set()
        one_sums = set()

        

        for i in range(n -1, - 1)





sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
