//
// Created by giangtran on 09/05/2018.
//

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;
string s;
int main(){
    ios::sync_with_stdio(false); cin.tie(0);
    while(true){
        cin>>s;
        if(s.compare("#") == 0){
            break;
        }
        if(next_permutation(s.begin(), s.end())){
            cout<<s<<endl;
        }else{
            cout<<"No Successor"<<endl;
        }
    }
    return 0;
}
