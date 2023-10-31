x = input()
mp = {}
mp[1] = {2, 4}
mp[2] = {1, 3, 5}
mp[3] = {2, 6}
mp[4] = {1, 5, 7}
mp[5] = {2, 4, 6, 8}
mp[6] = {3, 5, 9}
mp[7] = {4, 8}
mp[8] = {5, 7, 9, 0}
mp[9] = {6, 8}
mp[0] = {8}
flag = True;
for i in range(1, len(x)):
    if not(int(x[i]) in mp[int(x[i - 1])]):
        flag = False
print("YES" if flag else "NO")
