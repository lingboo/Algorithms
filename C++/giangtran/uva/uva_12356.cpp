//
// Created by giangtran on 07/05/2018.
//

#include <cstdio>
#include <iostream>

using namespace std;

int main(){
    int S, B, L, R;
    while(scanf("%d %d", &S, &B), (S || B)){
        int left[S + 5];
        int right[S + 5];
        for(int i = 1; i <= S; ++i){
            left[i] = i - 1;
            right[i] = i + 1;
        }
        left[1] = -1;
        right[S] = -1;
        for(int i = 0; i < B; ++i){
            scanf("%d %d", &L, &R);
            left[right[R]] = left[L];
            if(left[L] != -1)
                printf("%d ",left[L]);
            else
                printf("* ");
            right[left[L]] = right[R];
            if(right[R] != -1)
                printf("%d\n", right[R]);
            else
                printf("*\n");
        }
        printf("-\n");

    }
    return 0;
}