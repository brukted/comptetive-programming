n = int(input())

arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

start = None
end = None

hasStarted = False

for idx in range(n):
    if arr[idx] != sorted_arr[idx]:
        if hasStarted:
            end = idx
            continue

        start = idx
        end = idx
        hasStarted = True

if not hasStarted:
    print("yes")
    print(1, 1)
    exit()

i = start
j = end

while i <= end:
    if arr[i] != sorted_arr[j]:
        print("no")
        exit()
    i += 1
    j -= 1

print("yes")
print(start + 1, end + 1)
