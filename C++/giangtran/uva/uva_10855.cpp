//
// Created by giangtran on 08/05/2018.
//

#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    int N, n;
    while(scanf("%d %d", &N, &n), (N || n)){
        vector<string> bs;
        vector<string> ms;
        vector<string> total[4];
        int result[4];
        string lbs;
        string lms;
        string sample = "";
        cin.ignore();
        for (int i = 0; i < N; ++i) {
            getline(cin,lbs);
            bs.push_back(lbs);
        }
        for(int i = 0; i < n; ++i){
            getline(cin, lms);
            ms.push_back(lms);
            sample += lms;
        }
        total[0] = bs;
        for(int i = 1; i < 4; ++i){
            total[i] = total[i-1];
            for(int k = 0; k < N; ++k){
                for(int l = 0; l < N; ++l){
                    total[i][k][l] = total[i-1][l][N-1-k];
                }
            }
        }
        string temp;
        for(int i = 0; i < 4; ++i){
            result[i] = 0;
            for (int k = 0; k <= N-n; ++k) {
                for (int l = 0; l <= N-n ; ++l) {
                    temp = "";
                    for(int m = k ; m <= k+n-1;++m){
                        temp += total[i][m].substr(l, n);
                    }
                    if(temp.compare(sample) == 0){
                        result[i]++;
                    }
                }
            }
        }
        for(int i = 0; i < 4;++i){
            cout<<result[i]<<(i < 3 ? " " : "\n");
        }

    }
    return 0;
}