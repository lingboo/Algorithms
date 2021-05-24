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

// factorial(n) = 1                if n <= 0
//              = factorial(n-1)*n if n > 0
//
int factorial(int n){
    if(n > 0){
        return factorial(n-1)*n;
    }
    return 1;
}

int num_combination(int n, int k){
    int t1 = factorial(n);
    int t2 = factorial(k);
    int t3 = factorial(n-k);
    return t1/(t2*t3);
}

void fill_in_array(int *A, int value){
    int n = sizeof(*A)/sizeof(int);
    for(int i=0; i < n; i++){
        A[i] = value;
    }
}

void fill_in_2darray(int *A, int size, int value){
    for(int i=0; i<size;i++){
        for(int j=0; j<k;j++){
            A[i*k+j] = value;
        }
    }
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

void combination(int k, int left, int right, int tree_height, int a[tree_height]){
    static int count = 0;
    if(tree_height >= k){
        for(int ind=0; ind<tree_height; ind++){
            //p_comb[count] = A[a[ind]];
        } 
        return;
    }
    int j=0;
    for(int i=left; i<right; i++){
        a[j]=i;
        combination(k, i+1, right, tree_height+1, a);
        j++;
    }
}

void TOH(int n, char a, char b, char c){
    if(n>0){
        TOH(n-1, a, c, b);
        printf("From %c to %c", a, c);
        TOH(n-1, b, a, c);
    }
}

int fun(int n=1){
    int x=1, k;
    if(n==1) return x;
    for(k=1; k<n; k++)
        x = x + fun(k) * fun(n-k);
    return x;
}

void test(int * c){
    cout<<*(c+2);
}

int main(){
    //int x = 5;
    //cout<<fun4(x)<<endl;
    //double  n = 1;
    //int m = 10;
    //cout<<taylor_series_reduce(n, m)<<endl;
    //fill_in_array(F, 20, -1);    
    //cout<<memoization_fib(6)<<endl;
    
    const int C = num_combination(n, k);
    int comb[C][k];
    fill_in_2darray(&comb[0][0], C, 100);
    cout<<comb[0][0]<<endl;
    char * c;
    int *const b = comb[0];
    comb[1][1] = 200;
    cout<<b[k+1]<<endl;

    int A[] = {1, 3, 4};
    test(A);
    //combination(A, comb, n, k);
    // cout<<fun(5)<<endl;
}
