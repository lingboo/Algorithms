//
// Created by giangtran on 07/05/2018.
//
#include <algorithm>
#include <iostream>

using namespace std;
typedef long long ll;

bool compare(ll a, ll b){
    ll x = 0, y = 0;
    while(a%3 ==0 ){
        a/=3;
        x++;
    }
    while(b%3 ==0){
        b/=3;
        y++;
    }
    if (x==y)
        return a < b;
    return x > y;
}

int main(){
    int n;
    scanf("%d", &n);
    ll arr[n];
    for(int i = 0; i < n; i++){
        scanf("%lld", &arr[i]);
    }
    sort(arr, arr+n, compare);
    for(int i = 0; i < n; i++){
        cout<<arr[i]<<(i == n - 1  ? "":" ");
    }
    return 0;
}
