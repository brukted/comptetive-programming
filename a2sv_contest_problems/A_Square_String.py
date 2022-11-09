print(*map(lambda x: "YES" if x else "NO", map(lambda s: not(len(s) %
      2 == 1 or s[:len(s) // 2] != s[len(s) // 2:]), map(lambda _: input(), range(int(input()))))), sep='\n')
