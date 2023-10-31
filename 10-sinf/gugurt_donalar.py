from math import *
n, a, b = map(int, input().split())
while n > 0:
    x = int(input())
    c = sqrt(a * a + b * b)
    if c >= x:
        print("BOX")
    else:
        print("TRASH")
    n -= 1
