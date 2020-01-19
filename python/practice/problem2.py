n = int(input())
s = list(map(int,input().split()))
i = 0
x = 0
while(i<n-1):
    a = 1
    if(i<n-2):
        if(s[i+2]==0):
            x = x+1
            i = i+2
            a = 0
    if(a!=0):
        if(s[i+1]==0):
            x = x+1
            i = i+1
print(x)
