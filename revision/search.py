def linearSearch(a,key):
    for i,j in enumerate(a):
        if key==j:
            print(str(key)+" found at index "+str(i))
            return True
    return False

def  binarySearch(a,key):
    l = 0 
    r = len(a)-1
    while l<=r:
        x = l+(r-1)//2
        if(a[x]==key):
            print(str(key)+" found at index "+str(x))
            return True
        elif(a[x]<key):
            l=x+1
        else:
            r = x-1
    return False

if __name__ == "__main__" :
    a = list(map(int,input().split()))
    key = int(input())
    print("Linear Search: "+str(linearSearch(a,key)))
    print("Binary Search: "+str(binarySearch(sorted(a),key)))
