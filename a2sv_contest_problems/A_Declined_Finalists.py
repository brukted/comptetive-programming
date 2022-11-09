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


k = sng_int()
ranks = int_list()

ranks.sort()

should_be = 1
skipped = 0

for r in ranks:
    fst_print(r - should_be)
    skipped += r - should_be
    should_be = r + 1

fst_print(skipped)
