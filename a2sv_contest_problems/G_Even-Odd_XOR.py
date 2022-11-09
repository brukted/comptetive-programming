from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    ans = [0]
    even_xor = 0
    odd_xor = 0

    for i in range(1, n + 1):
        ans.append(i)
        if i % 2 == 1:
            odd_xor ^= i
        else:
            even_xor ^= i

    if odd_xor == even_xor:
        print(*ans[1:])
        continue

    if n % 2 == 0:
        lst_odd = n - 1
        lst_even = n
    else:
        lst_odd = n
        lst_even = n - 1

    odd_xor ^= lst_odd
    ans[lst_odd] = even_xor ^ odd_xor
    

    if ans[lst_odd] <= n:
        while lst_even == ans[lst_odd]:
            lst_even -= 2
        
        even_xor ^= ans[lst_even]
        ans[lst_even] ^= 1 << 30
        ans[lst_odd] ^= 1 << 30
        even_xor ^= ans[lst_even]
    
    odd_xor ^= ans[lst_odd]

    print(*ans[1:])

    # print("#", even_xor, odd_xor, even_xor == odd_xor)
