//
// Created by giangtran on 07/05/2018.
//

#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        int arr[n];
        bool flag[3000];
        int count = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &arr[i]);
            flag[i] = false;
        }
        if(n == 1){
            count++;
        }else{
            for(int i = 0; i < n -1; ++i){
                int t = abs(arr[i+1] - arr[i]);
                if((1 <= t && t < n) && !flag[t - 1]){
                    flag[t - 1] = true;
                    count++;
                }

            }
        }

        if(count >= n - 1){
            cout<<"Jolly"<<endl;
        }else{
            cout<<"Not jolly"<<endl;
        }
    }
    return 0;
}
