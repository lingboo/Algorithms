//
// File: /Users/trangiang/Learning/reference.cpp
//
// Created by Giang Tran on 2021 Apr 16 10:27:06.
//

#include<cstdio>
#include<iostream> 

using namespace std;

int main(){
    int a = 10;
    int &r = a;
    r = 20;
    int b = 50;
    r = b;
    cout<<a<<endl;
    cout<<r<<endl;
    return 0;
}
