#include<iostream>
#include<algorithm>
using namespace std;
int main() {
  int t;
  cin >> t ;
  string d;
  getline(cin,d);
  int r[t]={1};
  for(int i=0;i<t;i++){
    string s,t,p;
    getline(cin,s);
    getline(cin,t);
    getline(cin,p);
    int a[s.length()]={0},b[t.length()]={0},c[p.length()]={0};
    int z=0;
    for(int j=0;j<t.length();j++){
      while(z<s.length()&&b[j]==0){
        if(t[j]==s[z]&&a[z]==0){
          b[j]=1;a[z]=1;
          r[i]=1;
          z++;
        }
        else{
          r[i]=0;
          break;
        }
      }
      for(int k=0;k<p.length()&&b[j]==0;k++){
        if(t[j]==p[k]&&c[k]==0){
          b[j]=1;c[k]=1;
          r[i]=1;
        }
        else{
          r[i]=0;
        }
      }
    }
    for(int k=0;k<s.length();k++){
      if(a[k]==0){
        r[i]=0;
        break;
      }
    }
  }
  for(int i=0;i<t;i++){
    if(r[i]==1){
      cout << "YES\n";
    }
    else{
      cout << "NO\n";
    }
  }
  return 0;
}
