def solution(l):
    n= len(2)
    if n==2 :
        return [1,1]
    else:
        a = l[0]
        b = 0
        c = l[n-1]
        for i in range(1,n-1):
            b+=l[i]
        b = b/n-2
        


    
    return [-1,-1]


if __name__ == '__main__':
    l = list(map(int,input().split()))
    print(solution(l))