from math import cos, sin, sqrt


w = float(input())


def ans(t): return sqrt((w - t) ** 2 + (cos(w + t) - 1 - cos(t)
                                        ) ** 2 + (sin(w + t) - sin(t)) ** 2)


best = w
curr = ans(w)
step = 2.0

for i in range(10 ** 3):
    if step == 0.0:
        break

    if ans(best + step) < curr:
        curr = ans(best + step)
        best += step
    elif best - step > 0 and ans(best - step) < curr:
        curr = ans(best - step)
        best -= step
    else:
        step /= 2.0

print(curr)
