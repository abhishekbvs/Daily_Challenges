b,p,f = list(map(int,input().split()))
h,c = list(map(int,input().split()))
x = 0
if(h>=c):
    a1 = 1
else:
    a1 = 0
while( p>=1 and f>=1 and b >= 2 ):
    if(a1 == 1):
        if(p>=1):
            p = p - 1
            b = b - 2
            x = x + h
        else:
            a1 = 0
    elif(a1 == 0):
        if(f>=1):
            f = f - 1
            b = b - 2
            x = x + c
        else:
            a1 = 1
print(x)