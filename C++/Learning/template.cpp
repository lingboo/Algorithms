//
// File: /Users/trangiang/Algorithms/C++/Learning/template.cpp
//
// Created by Giang Tran on 2021 Apr 18 10:42:38.
//

#include<cstdio>
#include<iostream> 

using namespace std;

template<class T> class Arithmatic{
private:
    T a;
    T b;
public:
    static int num_arithmatic;

    Arithmatic<T>(T _a, T _b){
        a = _a;
        b = _b;
    }
    T add(){
        return a+b;
    }
    T sub(){
        return a-b;
    }
};

int main(){
    Arithmatic<int> r1(10, 50);
    cout<<r1.add()<<endl;

    Arithmatic<float> r2(30.6, 50.4);
    cout<<r2.sub()<<endl;
    return 0;
}

