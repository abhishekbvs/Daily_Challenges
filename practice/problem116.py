t = int(input())
for i in range(0,t):
    a = list(map(int,input().split()))
    if (a[2]%3==0):
        print(a[0])
    elif(a[2]%3==1):
        print(a[1])
    elif(a[2]%3==2):
        print(a[0]^a[1])

    