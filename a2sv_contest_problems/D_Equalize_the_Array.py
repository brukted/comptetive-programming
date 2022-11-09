from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    countHeights = list(Counter(a).values())

    totalHeightSum = sum(countHeights)
    
    countOfCounts = list(Counter(countHeights).items()) # countHeight, count

    countOfCounts.sort(reverse= True)

    largerRemovalCost = 0
    lowerRemovalCost = totalHeightSum
    prevCount = 0

    prevHeight = countOfCounts[0][0]

    minn = float('inf')

    for idx, (height, count) in enumerate(countOfCounts):
        largerRemovalCost += prevCount * abs(height  - prevHeight)
        lowerRemovalCost -= height * count

        cost = largerRemovalCost + lowerRemovalCost # cost to make all curr height

        minn = min(minn, cost)

        prevHeight = height
        prevCount += count

    print(minn)



