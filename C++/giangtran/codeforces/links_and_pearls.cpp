//
// Created by giangtran on 09/05/2018.
//

#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main(){
    string s;
    int links = 0;
    int pearls = 0;
    cin>>s;
    for(int i = 0; i < s.size(); ++i){
        if(s[i] == '-'){
            links++;
        }else{
            pearls++;
        }
    }
    if(links == s.size() || links % pearls == 0){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
    return 0;
}