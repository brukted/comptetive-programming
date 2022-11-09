# BEGIN Template
def single_int(): return int(input())
def int_list(): return list(map(int, input().split()))
def char_list(): return list(input())
# BEGIN Template


t = single_int()

for _ in range(t):
    n = single_int()
    if n <= 30:
        print('NO')
    else:
        print('YES')
        print('6', '14', '10', n - 30)