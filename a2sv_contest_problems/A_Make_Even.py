t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 0:
        print("0")
        continue

    digits = map(int, str(n))
    even_index = -1

    for idx, digit in enumerate(digits):
        if digit % 2 == 0:
            even_index = idx
            break
    
    if even_index == -1:
        print("-1")
    elif even_index == 0:
        print("1")
    else:
        print("2")

