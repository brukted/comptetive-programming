t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    stack = []

    for ch in s:
        if stack and ch == ")" and stack[-1] == '(':
            stack.pop()
            continue

        else:
            stack.append(ch)

    print(len(stack)//2)
