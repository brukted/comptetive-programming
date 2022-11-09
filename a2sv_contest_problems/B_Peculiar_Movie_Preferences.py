def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        latest_middle = -1
        least_idx = {}
        found = False

        for i in range(n):
            s = input()

            if s[::-1] in least_idx and least_idx[s[::-1]] < latest_middle:
                found = True
                break

            latest_middle = i if s == s[::-1] else latest_middle

            if s not in least_idx:
                least_idx[s] = i

        print('YES' if found else 'NO')


main()
