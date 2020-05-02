def solution(l,t):
    n = len(l)
    a = [-1,-1]
    x = 0
    y = 0
    s = l[0]
    while x<n or y<n:
        if s == t:
            return [x,y]
        elif s < t:
            y+=1
            if y==n:
                break
            s+=l[y]
        else:
            s-=l[x]
            x+=1         
    return a

if __name__ == '__main__':
    l = list(map(int,input().split()))
    t = int(input())
    print(solution(l,t))