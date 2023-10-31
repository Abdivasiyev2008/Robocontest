n, m, a, b = map(int, input().split())
x = []
z = ""
result = []
for i in range(1, n+1):
    img = input().split()
    x += img

for i in x:
    for j in i:
        z += j * b

    result += z.split()
    z = ""


for i in result:
    for j in range(1, a+1):
        print(i)
