#include <iostream>
using namespace std;

int main() {
  int n,m;
   cin >> n >> m;
   int x = n;
   int i = 0;
   while(x<m){
     x = x*3;
     i++;
   }
   int result;
   int r = -1;
   int a;
   while(x>n){
     if(x==m)
     {
       r = i;
       break;
     }
     else{
       a = x/3;
       i--;
       int j = 0;
       while(a<m)
       {
          a = a*2;
          j++;
        }
        if(a==m)
          { x=a;
            i=i+j;}
        else
          x = x/3;
    }
   }
   if (m==n)
    r=0;
   cout << r ;
}
