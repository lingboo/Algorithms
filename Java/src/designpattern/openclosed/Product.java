package designpattern.openclosed;


public class Product {
    String name;
    Color color;
    Size size;

    public Product(String name, Color color, Size size){
        this.name = name;
        this.color = color;
        this.size = size;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Product: " + name + ", Size: " + this.size + ", Color: " + this.color;
    }
}
