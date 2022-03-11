t = int(input())

for _ in range(t):
    n = int(input())
    sequence = sorted(list(map(int,input().split())))
    i = 0 # Next blue painted index
    j = len(sequence) - 1 # Next red painted index
    red_sum = 0
    red_count = 0
    blue_sum = 0
    blue_count = 0
    result = "NO"

    while i <= j:
        if red_sum <= blue_sum:
            red_sum += sequence[j]
            red_count += 1
            j -= 1
        elif red_count >= blue_count:
            blue_sum += sequence[i]
            blue_count += 1
            i += 1
        
        if red_sum > blue_sum and red_count < blue_count:
            result = "YES"
            break
    
    print(result)