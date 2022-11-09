a = input().lower()
b = input().lower()

for i in range(len(a)):
    if a[i] == b[i]:
        continue

    if a[i] < b[i]:
        print("-1")
    elif a[i] > b[i]:
        print("1")
    exit()

print("0")