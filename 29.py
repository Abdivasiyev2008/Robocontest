from math import *
n=int(input())
m = []

for i in range(1, n + 1):
    m.append(int(input()))

for k in m:
    s = 0

    for j in range(1, int(sqrt(k)) + 1):
        if k % j == 0:
            if j % 2 == 0:
                s += 1
            if j != k // j and k % (k // j) == 0 and (k // j) % 2 == 0:
                s += 1
    print(s)
