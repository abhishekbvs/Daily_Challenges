#include<iostream>
#include<algorithm>
using namespace std;
int main(){
  int t,n,x;
  cin >> t;
  int r[t];
  for(int i=0;i<t;i++){
    cin >> n >>x;
    r[i]=x*2;
  }
  for(int i=0;i<t;i++){
    cout << r[i] <<"\n";
  }
}
