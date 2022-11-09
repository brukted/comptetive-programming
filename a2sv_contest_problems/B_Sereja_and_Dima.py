n = int(input())
cards = list(map(int, input().split()))

i = 0
j = n - 1

sums = [0 , 0]
turn = 0

while i <= j:
    if cards[i] > cards[j]:
        sums[turn] += cards[i]
        i += 1
    else:
        sums[turn] += cards[j]
        j -= 1
    
    turn = (turn + 1) % 2

print(sums[0], sums[1])