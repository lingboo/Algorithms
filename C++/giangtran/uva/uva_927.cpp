//
// Created by giangtran on 06/05/2018.
//

#include <algorithm>
#include <stdio.h>
using namespace std;
int T, n;

int sum(int b[], int n){
    int s = 0;
    for(int i = 1; i < n; i++){
        s += b[i];
    }
    return s;
}

int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d", &n);
        int a[n];
        for(int i = 0; i < n; i++){
            scanf("%d", &a[i]);
        }
        int b[n];
        for(int i = 1; i < n; i++){
            int temp = 0;
            for(int j = 0; j < i; j++){
                if(a[i] >= a[j]){
                    temp++;
                }
            }
            b[i] = temp;
        }
        printf("%d\n",sum(b, n));
    }
    return 0;
}

