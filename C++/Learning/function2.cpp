//
// File: /Users/trangiang/Learning/function2.cpp
//
// Created by Giang Tran on 2021 Apr 16 15:26:24.
//

#include<cstdio>
#include<iostream> 

using namespace std;

struct Rectangle{
    int length;
    int breadth;
};

int area(Rectangle *r1){
    r1->length++;
    return r1->length*r1->breadth;
}

struct Test{
    int A[5];
    int n;
};

void modify_struct(Test *t1){
    for(int i = 0; i < 5; i++){
        t1->A[i] = i*i;
    }
    for(int a: t1->A){
        cout<<a<<" ";
    }
}

Rectangle * create_struct_in_heap(int size){
    Rectangle *r1;
    r1 = (Rectangle *) malloc(sizeof(Rectangle));
    r1->breadth = 20;
    r1->length = 50;
    return r1;
}

int main(){
    //Rectangle r = {10, 5};
    //int a = area(&r);
    //cout<<a<<endl;
    //cout<<r.length<<endl;
    //-----------------------------
    Test t = {{3, 20, 55, 98, 6}, 6};
    modify_struct(&t);
    for(int x: t.A){
        cout<<x<<endl;
    }
    return 0;
}
