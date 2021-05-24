//
// File: /Users/trangiang/Learning/class.cpp
//
// Created by Giang Tran on 2021 Apr 16 16:07:26.
//

#include<cstdio>
#include<iostream> 
#include<math.h>

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

    bool operator==(Rectangle a){
        return length == a.length && breadth == a.breadth;
    }
    
    bool operator!=(Rectangle a){
        return !(length == a.length && breadth == a.breadth);
    }

    ostream& operator<<(ostream& s){
        return s<<"Length: "<<length<<". Breadth: "<< breadth;
    }
};

int Rectangle::num_rectangle = 0;
int main(){
    //Rectangle *r1 = new Rectangle(40, 30);
    //cout<<Rectangle::num_rectangle<<endl;
    //cout<<r1->area()<<endl;
    //Rectangle r2(20, 5);
    //cout<<Rectangle::num_rectangle<<endl;
    //cout<<r2.area()<<endl;
    //free(r1);
    // unsigned int x[4][3] = {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};
    // printf("%u,%u,%u", x+3, *(x+3), *(x+2)+3);
    Rectangle r(20, 50);
    r<<"kk";
    return 0;
}
