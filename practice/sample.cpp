#include <iostream>
using namespace std;
int main() {
  int k;
  cin >> k;
  int r[k];
  for(int i = 0; i < k; i++){
    int n, s, t;
    cin >> n >> s >> t;
    int r1 = s+t-n;
    s=s-r1;
    t=t-r1;
    if(r1==n){
      r[i]=1;
    }
    else{
      if(s>t){
        r[i]=s+1;
      }
      else{
        r[i]=t+1;
      }
    }
  }
  for(int i = 0; i < k; i++){
    cout << r[i] << endl;
  }
  return 0;
}


  // cin >>
  // cout <<
  // for(int i=0; i<n; i++){}
  // int arr[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 0};
  // int n = sizeof(arr)/sizeof(arr[0]);
  //   sort(arr, arr+n); // Ascending
  //   sort(arr, arr+n, greater<int>()); // descending
  //   cout << "\nArray after sorting using "
  //        "default sort is : \n";
  //   for (int i = 0; i < n; ++i)
  //       cout << arr[i] << " ";

  //  struct Interval
  //  {
  //     int start, end;
  //  };
  //
  //   // Compares two intervals according to staring times.
  //  bool compareInterval(Interval i1, Interval i2)
  //  {
  //       return (i1.start < i2.start);
  //  }
  //
  //  int main()
  //  {
  //     Interval arr[] =  { {6,8}, {1,9}, {2,4}, {4,7} };
  //     int n = sizeof(arr)/sizeof(arr[0]);
  //
  //     // sort the intervals in increasing order of
  //     // start time
  //     sort(arr, arr+n, compareInterval);
  //
  //     cout << "Intervals sorted by start time : \n";
  //     for (int i=0; i<n; i++)
  //        cout << "[" << arr[i].start << "," << arr[i].end
  //             << "] ";
  // }
