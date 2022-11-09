t = int(input())

for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    al = list(a)
    two_sums = set()

    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                two_sums.add(al[i]+al[j])

    f = False
    while j < len(two_sums):
        for i in range(len(al)):
            

            
