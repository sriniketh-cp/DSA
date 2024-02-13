1.Linear search
#include <iostream>
using namespace std;
int main() {

    int target;
    int arr[100];
    int i;
    int flag=0;
    cin>>target;
    cout<<"please enter the array and the target to find the target"<<endl;
    for(i=0;i<5;i++) {
        cin>>arr[i];
      if(arr[i]==target){
        flag=1;
      }
    }
    if(flag==1) {
            cout<<"target is found"<<endl;
    } else{
            cout<<"target is not found"<<endl;
     }
} 

2.single number
def navive(arr):
    for i in range(arr):
        singlecount=0
    for j in range(arr):
        if(arr[i]==arr[j]):
            singlecount=1

        if(singlecount ==1):
            return arr[i];

    return -1;
