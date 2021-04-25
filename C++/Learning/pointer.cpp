//
// File: /Users/trangiang/Learning/pointer.cpp
//
// Created by Giang Tran on 2021 Apr 15 15:35:10.
//

#include<cstdio>
#include <cstdlib>
#include<iostream> 
#include <malloc/_malloc.h>
#include<stdlib.h>

using namespace std;

struct Rectengle{
    int length;
    int breadth;
};

void fill_in_array(int *A, int n, int value){
    for(int i=0; i<n; i++){
        A[i] = value;
    }
}
int F[20];

int main(){
    //int *p = (int *) malloc(5*sizeof(int));
    //p[0] = 1; p[1] = 5; p[2] = 20; p[3] = 55; p[4] = 200;
    //for(int i=0; i < 5; i++) cout<<p[i]<<endl;

    //int *p1;
    //float *p2;
    //char *p3;
    //struct Rectengle *p4;

    //cout<<sizeof(p1)<<endl;
    //cout<<sizeof(p2)<<endl;
    //cout<<sizeof(p3)<<endl;
    //cout<<sizeof(p4)<<endl;
    Rectengle r = {10, 5};
    Rectengle *p = &r;
    
    p->breadth = 15;
    r.length = 20;
    cout<<p->length<<endl;
    cout<<r.breadth<<endl;
    
    p = (Rectengle *) malloc(sizeof(Rectengle));
    p->length = 50;
    p->breadth = 200; 
    cout<<p->breadth<<endl;
    cout<<p->length<<endl;
    free(p);

    cout<<F[10]<<endl;
    fill_in_array(F, 20, -1);
    cout<<F[10]<<endl;
    return 0;
}
