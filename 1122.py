n = input()
s = []
for i in n:
    if int(i) % 2 != 0:
        s.append(i)
if (len(s) == len(n)) and (len(s) % 2 != 0):
    print("YES")
else:
    print("NO")
