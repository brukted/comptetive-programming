n = int(input())
arr = list(map(int, input().split()))

longest = {}

prev = [i for i in range(n)]

for idx, i in enumerate(arr):
    if i not in longest:
        longest[i] = [1, idx]

    if i - 1 in longest:
        if longest[i-1][0] + 1 > longest[i][0]:
            longest[i] = [longest[i-1][0] + 1, idx]
            prev[idx] = longest[i-1][1]

end_val = 0
end_i = 0

for lg, i in longest.values():
    if lg > end_val:
        end_val = lg
        end_i = i

ans = []

while prev[end_i] != end_i:
    ans.append(end_i + 1)
    end_i = prev[end_i]

# print(prev)

ans.append(end_i + 1)
ans.reverse()

print(end_val)
print(' '.join(map(str, ans)))
