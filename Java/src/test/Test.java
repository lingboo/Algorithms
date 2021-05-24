//
// File: /Users/trangiang/Algorithms/Java/test.java
//
// Created by Giang Tran on 2021 Apr 27 15:04:17.
//
package test;

class Test{
    
    static void use(Dog d){
        d.bark();
        if(d instanceof Callable){
            d.call();
        }
    }
    public static void main(String args[]){
        Bird bird = new Bird();
        Husky dog = new Husky();
        // use(bird);
        use(dog);
    }
}

