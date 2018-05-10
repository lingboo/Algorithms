//
// Created by giangtran on 07/05/2018.
//
#include <algorithm>
#include <iostream>

using namespace std;
int n, k;
int main(){
    scanf("%d %d", &n, &k);
    while(n){
        int a = n % 10;
        if(k <= a || k == 0){
            n -= k;
            printf("%d", n);
            return 0;
        }
        k -= a;
        n /= 10;
        k -= 1;
    }
    return 0;
}

