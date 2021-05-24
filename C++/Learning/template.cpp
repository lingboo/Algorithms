//
// File: /Users/trangiang/Algorithms/C++/Learning/template.cpp
//
// Created by Giang Tran on 2021 Apr 18 10:42:38.
//

#include<cstdio>
#include<iostream> 

using namespace std;

template<typename T, typename V> class Arithmatic{
private:
    T a;
    T b;
    V c;
public:
    static int num_arithmatic;

    Arithmatic<T, V>(T _a, T _b, V _c){
        a = _a;
        b = _b;
        c = _c;
    }
    T add(){
        return a+b;
    }
    T sub(){
        return a-b;
    }
    void hello(){
        cout<<c<<endl;
    }
};

template<typename Oper>
void loop(int *a, Oper op){
    for(int i=0; i<5; i++){
        cout<<op(i)<<endl;
    }
}

int main(){
    Arithmatic<int, char> r1(10, 50, 'G');
    cout<<r1.add()<<endl;
    r1.hello();

    Arithmatic<float, int> r2(30.6, 50.4, 50);
    cout<<r2.sub()<<endl;
    r2.hello();

    int A[] = {3, 6, 4, 7, 8};
    loop(A, 
        [](int x){
            return x<5;
        }
        );
    return 0;
}

