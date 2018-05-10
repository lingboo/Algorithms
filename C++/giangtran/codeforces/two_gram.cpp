//
// Created by giangtran on 07/05/2018.
//

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int n;
string s;
vector<int> v;
map<string, int> mapped;
int main(){
    scanf("%d", &n);
    cin>>s;
    map<string, int>::iterator it;
    for(int i = 0; i < n - 1; i++){
        string t(s, i, 2);
        it = mapped.find(t);
        if(it == mapped.end()){
            mapped[t] = 1;
        }else{
            mapped[t] ++;
        }
    }
    int max_ =  0;
    string result = "";
    for(it = mapped.begin(); it != mapped.end(); it++){
        if(it->second > max_){
            max_ = it->second;
            result = it->first;
        }
    }
    cout<<result;
}