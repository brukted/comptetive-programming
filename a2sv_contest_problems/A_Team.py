print(
    sum(
        1
        for _ in filter(
            lambda x: x >= 2,
            map(lambda _: sum(map(int, input().split())), range(int(input()))),
        )
    )
)
