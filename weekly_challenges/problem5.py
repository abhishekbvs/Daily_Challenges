t = int(input())
for i in range(t):
    xx = input()
    a = list(xx)
    x = len(a)
    if(x==1):
        print(a[0])
    else:
        z = 9*(x-1)
        ss = int(''.join(a[0] for i in range(0,x)))
        if(int(xx)<ss):
            z = z + int(a[0])-1
        else:
            z = z + int(a[0])
        print(z)