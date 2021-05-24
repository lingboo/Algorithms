package test;

abstract class Dog implements Callable{
    @Override
    public void call() {
        // TODO Auto-generated method stub
        System.out.println("I'm a dog");
    }
    abstract void bark();
}