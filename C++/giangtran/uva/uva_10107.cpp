//
// Created by giangtran on 09/05/2018.
//

#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
void swap(ll &a, ll&b){
    int temp = a;
    a = b;
    b = temp;
}
int main(){
    vector<ll> series;
    ll X;
    int n;
    ll res;
    while(scanf("%lld", &X) != EOF){
        series.push_back(X);
        n = series.size();
        int temp_n = n;
        while(temp_n > 1 && series[temp_n-1] < series[temp_n-2]){
            swap(series[temp_n-1], series[temp_n-2]);
            temp_n--;
        }
        if(n == 1){
            cout<<series[0]<<endl;
            continue;
        }
        if(n % 2 == 0){
            res = (series[n/2-1]+series[n/2])/2;
        }else{
            res = series[n/2];
        }
        cout<<res<<endl;
    }
    return 0;
}