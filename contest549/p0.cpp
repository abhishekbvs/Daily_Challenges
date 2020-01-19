#include <iostream>
using namespace std;
int main() {

  int n,x,y,result;
  cin >> n;
  int a[n];
  for (int i=0; i<n; i++){
    cin >> a[i];
    if(a[i]==0){
      x = i;
    }
    else if(a[i]==1){
      y = i;
    }
  }
  if(a[n-1]==0){
    result = y+1;
  }
  else if (a[n-1]==1){
    result = x+1;
  }
  cout << result;
  return 0;
}
