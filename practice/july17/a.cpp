#include <iostream>
using namespace std;
int main() {
  int t;
  cin >> t;
  while(t--){
    int n;
    cin >> n;
    int a[n];
    int i=n;
    int s=0;
    int x = 0;
    while(i--){
      cin >> a[i];
      s=s+a[i];
    }
    int r,l = 0;
    for(int i=0;i<n;i++){
      if(i==0){
        r = 0;
        l = s - a[0];
      }
      else if(i==n-1){
        r = s - a[n-1];
        l = 0;
      }
      else{
        r = r+a[i-1];
        l = l-a[i];
      }
      if(r==l){
        x=1;
        break;
      }
    }
    if(x==1){
      cout << "YES";
    }
    else{
      cout << "NO";
    }
  }
}
