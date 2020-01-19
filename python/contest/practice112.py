n = int(input())
a = list(map(int,input().split()))
neg = 0
maxn = 0
maxp = 0
pos = 0
zero = 0
b=[]
a.sort()
for i in a:
    if i < 0 :
        neg+=1
        maxn+=abs(i)
        b.append(i)   
    elif i > 0:
        pos+=1
        maxp+=i
    else:
        zero+=1
x = 0
y = 0
if pos > 0:
    y = maxp-pos
if neg >=2 and neg%2==0:
    x = maxn-neg
elif neg>=1 and neg%2!=0:
    if zero > 0:
        x = maxn-neg + 1
        zero-=1
    else:
        x = maxn-neg + 2
elif neg==1 and neg%2!=0:
    x = maxn-1
print(x+y+zero)


