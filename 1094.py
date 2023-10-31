a = int(input())
number = 0

for i in range(1, a+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        number += i
    else:
        pass

print(number)
