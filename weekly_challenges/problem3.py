s = list(input())
m = ['h','e','l','l','o']
a = 0
for i in s:
    if(m[a]==i):
        a = a+1
    if a == 5:
        break 
if a == 5:
    print('YES')
else:
    print('NO')