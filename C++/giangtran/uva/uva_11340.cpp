//
// Created by giangtran on 07/05/2018.
//

#include <cstdio>
#include <unordered_map>
#include <iostream>

using namespace std;
typedef unordered_map<char, double> um;
int main(){
    int N, K, b, M;
    char a;
    um mapped;
    scanf("%d", &N);
    while(N--){
        double res = 0;
        scanf("%d", &K);
        while(K--){
            cin>>a>>b;
            mapped[a] = b;
        }
        scanf("%d", &M);
        string line;
        cin.ignore();
        while(M--){
            getline(cin, line);
            for(int i = 0; i < line.size(); i++){
                if(mapped.find(line[i]) != mapped.end()){
                    res += mapped[line[i]];
                }
            }
        }
        printf("%.2f$\n", res/100);
        mapped.clear();
    }
    return 0;
}