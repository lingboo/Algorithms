//
// Created by giangtran on 07/05/2018.
//

#include <algorithm>
#include <iostream>

using namespace std;
const int MAX = 2e5+5;
int arr[MAX];
int n, k;
int main(){
    scanf("%d %d", &n, &k);

    for(int i = 1; i <= n; i++){
        scanf("%d", &arr[i]);
    }
    sort(arr+1, arr+n+1);
    arr[0] = 1;
    arr[n+1] = 1e9 + 1;
    if(arr[k] < arr[k+1] ){
        cout<<arr[k]<<endl;
    }else{
        puts("-1");
    }
    return 0;
}