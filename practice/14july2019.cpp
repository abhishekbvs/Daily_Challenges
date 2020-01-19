#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  string input;
  cin >> input;
  int a=0,b=0;
  for(int i=0;i<n;i++){
    if(input[i]=='0'){
      a++;
    }
    else{
      b++;
    }
  }
  if(a!=b){
    cout << "1\n";
    cout << input;
  }
  else{
    cout << "2\n";
    cout << input[0] << " ";
    for(int i=1;i<n;i++){
      cout << input[i];
    }
  }
}
