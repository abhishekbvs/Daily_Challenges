def solution(s):
    a=""
    for x in s:
        if x==' ':
            a=a+"000000"
        else:
            if ord(x)<91 :
                a=a+"000001"
                i = ord(x)-64
            else:
                i = ord(x)-96
            d = {1:"1000",2:"1100",3:"1010",4:"1011",5:"1001",6:"1110",7:"1111",8:"1101",9:"0110",10:"0111"}
            if i<=10:
                a=a+d[i][0:2]+'0'+d[i][2:4]+'0'
            elif i<=20:
                a=a+d[i-10][0:2]+'1'+d[i-10][2:4]+'0'
            else:
                if i==23:
                    a=a+"010111"
                elif i<23:
                    a=a+d[i-20][0:2]+'1'+d[i-20][2:4]+'1'
                else:
                    a=a+d[i-21][0:2]+'1'+d[i-21][2:4]+'1'                  
    return a


if __name__== '__main__':
    print(solution(input()))