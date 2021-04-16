//
// File: /Users/trangiang/Learning/class.cpp
//
// Created by Giang Tran on 2021 Apr 16 16:07:26.
//

#include<cstdio>
#include<iostream> 

using namespace std;

class Rectangle{
    private:
    int length;
    int breadth;

    public:
    Rectangle(int l, int b){
        length = l;
        breadth = b;
    }

    int area(){
        return length*breadth;
    }

    void changeLength(int l){
        length = l;
    }
};

int main(){
    Rectangle *r = new Rectangle(20, 5);
    //Rectangle r(20, 5);
    cout<<r->area()<<endl;
    free(r);
    return 0;
}
