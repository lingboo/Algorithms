//
// File: /Users/trangiang/Learning/function.cpp
//
// Created by Giang Tran on 2021 Apr 16 13:21:47.
//

#include<cstdio>
#include<iostream> 
#include <malloc/_malloc.h>

using namespace std;

struct Student{
    int id;
    char name[10];
};

void pointer_swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void reference_swap(int &x, int &y){
    int temp = x;
    x = y;
    y = temp;
}

void student_swap(Student *s1, Student *s2){
    Student temp;
    temp = *s1;
    *s1 = *s2;
    *s2 = temp;
}

void student_swap_id(Student *s1, Student *s2){
    int  temp_id;

    temp_id = s1->id;
    s1->id = s2->id;
    s2->id = temp_id;
}

void change_array(int A[], int n){
    for(int i = 0; i < n; i++){
        A[i] = i*i;
    }
}

int * create_array_in_heap(int size){
    int *p;
    p = (int *) malloc(size*sizeof(int)); //p = new int[size];
    return p;
}

int main(){
    //int a = 5;
    //int b = 10;
    //cout<<&a<<endl;
    //cout<<&b<<endl;
    ////pointer_swap(&a, &b);
    //reference_swap(a, b);
    //cout<<&a<<endl;
    //cout<<&b<<endl;
    //printf("a: %d\n", a); 
    //printf("b: %d", b);
    //--------------------------------- 
    //
    //Student s1 = {1, "Giang"};
    //Student s2 = {2, "ACCC"};
    
    //cout<<s1.id<<" "<<s1.name<<endl;
    //cout<<s2.id<<" "<<s2.name<<endl;

    //student_swap_id(&s1, &s2);

    //cout<<s1.id<<" "<<s1.name<<endl;
    //cout<<s2.id<<" "<<s2.name<<endl;
    //---------------------------------
    //
    //int A[5] = {123, 5, 7, 2, 3};
    //change_array(A, 5);
    //for(int i = 0; i < 5; i++){
        //cout<<A[i]<<endl;
    //}
    int *A;
    A = create_array_in_heap(5);
    A[0] = 2;
    for(int i = 0; i < 5; i++){
        cout<<A[i]<<endl;
    }
 
    free(A);
    return 0;
}
