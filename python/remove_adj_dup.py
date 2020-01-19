t = int(input())
for i in range(t):
    s = list(input())
    a = []
    for i in s:
        if len(a) == 0:
            a.append(i)
        elif a[-1]!=i:
            a.append(i)
    print(str(a))