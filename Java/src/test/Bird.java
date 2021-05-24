//
// File: /Users/trangiang/Algorithms/Java/Bird.java
//
// Created by Giang Tran on 2021 Apr 27 15:06:33.
//
package test;

class Bird implements Callable{
    
    @Override
    public void call(){
        System.out.println("I am a bird");
    }
}
