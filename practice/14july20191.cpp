#include<iostream>
#include <algorithm>
using namespace std;
int main(){
  int n;
  cin >> n;
  int a[n];
  for(int i=0;i<n;i++){
    cin >> a[i] ;
  }
  sort(a,a+n);
  while(true){
    if(a[0]+a[n-2]>a[n-1]){
      cout << "YES\n";
      for(int i=0;i<n;i++){
        cout << a[i] << " ";
      }
    }
    else{
      int temp = a[n-1];
      a[n-1]=a[n-2];
      a[n-2]=temp;
    }
  }
  return 0;
}
