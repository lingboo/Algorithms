//
// File: /Users/trangiang/Algorithms/C++/Learning/recursion.cpp
//
// Created by Giang Tran on 2021 Apr 19 08:50:54.
//

#include<cstdio>
#include<iostream> 

using namespace std;

const int A[] = {4, 6, 7, 8};
const int n = 4;
const int k = 2;

void fill_in_array(int *A, int value){
    int n = sizeof(*A)/sizeof(int);
    for(int i=0; i < n; i++){
        A[i] = value;
    }
}

void fill_in_2darray(int (*A)[k], int value){
    int *p;
    cout<<sizeof(p)<<endl;
    cout<<sizeof(A[0])<<endl;
    cout<<*A[10]<<endl;
    int n = sizeof(A)/sizeof(A[0]);
    int m = sizeof(A[0])/sizeof(A[0][0]);
    cout<<n<<endl;
    cout<<m<<endl;
}

void fun1(int n){
    if(n > 0){
        printf("%d ", n);
        fun1(n-1);
    }
}

void fun2(int n){
    if(n > 0){
        fun2(n-1);
        printf("%d ", n);
    }
}

int fun3(int n){
    if(n > 0){
        return fun3(n-1)+n;
    }
    return 1;
}

int fun4(int n){
    static int x = 0;
    if(n > 0){
        x++;
        return fun4(n-1)+x;
    }
    return 0;
}
// A = [3, 4, 5, 6, 7] | n = 5 | k = 3 
// ==> comb = [[3, 4, 5], [3, 4, 6], [3, 4, 7], [4, 5, 6], [4, 5, 7], [5, 6, 7]]
//
//
//int ** recursive_combination(int *A, int n, int k){
    //for(int i = 0; i < n; i++){

    //}
    //return 
//}

// sum(n) = 0           if n <= 0
//        = sum(n-1)+n  if n > 0
//
int sum(int n){
    if(n > 0){
        return sum(n-1)+n;
    }
    return 0;
}
// factorial(n) = 1                if n <= 0
//              = factorial(n-1)*n if n > 0
//
int factorial(int n){
    if(n > 0){
        return factorial(n-1)*n;
    }
    return 1;
}

// power(m, n) = 1                 if n <= 1 
//             = power(m, n-1) * m if n > 1
// 
int power(int m, int n){
    if(n >= 1){
        return power(m, n-1)*m;
    }
    return 1;
}

int power1(int m, int n){
    if(n <= 0){
        return 1;
    }
    if(n%2 ==0){
        return power1(m*m, n/2);        
    }else{
        return power1(m, n-1)*m;
    }
}
// taylor_series c^x
// c^x = 1 + x/1 + x^2/2! + x^3/3! + .... + x^(n-1)/(n-1)! + x^n/n!
//
double taylor_series(int x, int n){
    static double p = 1;
    static double f = 1;
    if(n > 0){
        double r = taylor_series(x, n-1);
        p = p * x;
        f = f * n;
        return r + p/f;
    }
    return 1;
}

double taylor_series_reduce(double x, double n){
    static double S = 1;
    if(n <= 0){
        return S;
    }
    S = (1 + x/n)*S;
    return taylor_series_reduce(x, n-1);
}

int fib(int n){
    if(n <= 2){
        return 1;
    }
    return fib(n-1) + fib(n-2);
}

int F[20];
int memoization_fib(int n){
    if(n<=2){
        F[n] = 1;
        return F[n];
    }else{
        if(F[n-1] == -1){
            F[n-1] = memoization_fib(n-1);    
        }
        if(F[n-2] == -1){
            F[n-2] = memoization_fib(n-2);
        }
        F[n] = F[n-2] + F[n-1];
        return F[n];
    }
}
//                      1 (0C0)
//                    /   \
//              (1C0)1     1 (1C1) 
//                  / \   / \
//                 1  2(2C1) 1
//                / \  / \  / \
//               1    3   3    1
//              / \  / \ / \  / \
//             1   4    6   4    1
int num_pascal_triangle_combination(int n, int k){
    if(k == 0 || k == n){
        return 1;
    }
    return num_pascal_triangle_combination(n-1, k) + num_pascal_triangle_combination(n-1, k-1);
}

int num_combination(int n, int k){
    int t1 = factorial(n);
    int t2 = factorial(k);
    int t3 = factorial(n-k);
    return t1/(t2*t3);
}

void combination(int * A, int ** comb, int n, int k){
    int I[k];
    for(int i=0; i<n; i++){

    }
}

int main(){
    //int x = 5;
    //cout<<fun4(x)<<endl;
    //double  n = 1;
    //int m = 10;
    //cout<<taylor_series_reduce(n, m)<<endl;
    //fill_in_array(F, 20, -1);    
    //cout<<memoization_fib(6)<<endl;
    int C = num_combination(n, k);
    int comb[C][k];
    int (*p_comb)[k] = comb;
    for(int i=0; i<C; i++){
        for(int j=0; j<k; j++){
            comb[i][j] = i+j;
            cout<<&comb[i][j]<<": "<<comb[i][j]<<", ";
        }
    }
    cout<<p_comb[0][1]<<endl;
    fill_in_2darray(p_comb, -1);
    //combination(A, comb, n, k);
}
