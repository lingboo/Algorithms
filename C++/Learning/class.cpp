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

    static int num_rectangle;
    Rectangle(int l, int b){
        num_rectangle++;
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

int Rectangle::num_rectangle = 0;
int main(){
    Rectangle *r1 = new Rectangle(40, 30);
    cout<<Rectangle::num_rectangle<<endl;
    cout<<r1->area()<<endl;
    Rectangle r2(20, 5);
    cout<<Rectangle::num_rectangle<<endl;
    cout<<r2.area()<<endl;
    free(r1);
    return 0;
}
