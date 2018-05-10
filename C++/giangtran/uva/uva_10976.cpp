#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
//
// Created by giangtran on 06/05/2018.
//
using namespace std;
int T, D, Q;
typedef pair<int, int> _p;
typedef map<string, _p> map_10976;
int main(){
    scanf("%d", &T);
    while(T--){
        map_10976 mapped;
        scanf("%d", &D);
        char a[20];
        int b, c;
        while(D--){
            scanf("%s %d %d", &a, &b, &c);
            mapped[a] = _p (b, c);
        }
        scanf("%d", &Q);
        map_10976::iterator it;
        int q;
        while(Q--){
            string res = "UNDETERMINED";
            int count = 0;
            scanf("%d", &q);
            for(it = mapped.begin(); it!= mapped.end(); it++){
                string a = it->first;
                _p bc = it->second;
                int b = bc.first;
                int c = bc.second;
                if(b <= q && q <= c){
                    res = a;
                    count++;
                }
                if(count > 1){
                    res = "UNDETERMINED";
                    break;
                }
            }
            cout<<res<<"\n";
        }
        if(T > 0){
            printf("\n");
        }
        mapped.clear();
    }
    return 0;
}
