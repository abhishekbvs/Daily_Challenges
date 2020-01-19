#include <iostream>
using namespace std;
int main() {
  int n,num,product,product1,i,check;
  cin >> n;
  check = n;
  while(true){
    if(n%10==0){
      num = n-1;
      break;
    }
    else {
      if(n<10){
         num = n;
         break;
      }
      n--;
    }
  }
  product = 1;
  product1 = 1;
  while(num != 0)
  {
        product = product * (num % 10);
        num = num / 10;
  }
  while(check != 0)
  {
        product1 = product1 * (check % 10);
        check = check / 10;
  }
  if(product1>product){
    product = product1;
  }
  cout << product;
  return 0;
}
