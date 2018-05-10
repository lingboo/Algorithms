//
// Created by giangtran on 07/05/2018.
//
#include <algorithm>
#include <cstdio>
using namespace std;
int T;
int main(){
    scanf("%d", &T);
    int n, k;
    while(T--){
        scanf("%d %d", &n, &k);
        printf("%d\n", k ^ (k >> 1));
    }
    return 0;
}