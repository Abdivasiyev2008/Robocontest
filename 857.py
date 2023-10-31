a = int(input())
b = False
c = 0


if len(str(a)) == 9 and a[0]!=0:
    for i in str(a):
        c += int(i)

        if c % 2 == 1:
            b = True

        else:
            b = False


if b == True:
    print("yes")

else:
    print("no")
