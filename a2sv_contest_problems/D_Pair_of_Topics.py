topics =int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = zip(a,b)

ab.sort()

good_topics = 0

for i in range(topics):
    