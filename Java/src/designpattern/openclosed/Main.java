package designpattern.openclosed;

import java.util.ArrayList;

public class Main {
    
    public static void main(String[] args) {
        Product shoes = new Product("Shoes", Color.BLUE, Size.MEDIUM);
        Product wallet = new Product("Wallet", Color.RED, Size.SMALL);
        Product house = new Product("House", Color.BLUE, Size.LARGE);
        Product car = new Product("Car", Color.RED, Size.MEDIUM);

        ArrayList<Product> products = new ArrayList<>();
        products.add(shoes);
        products.add(wallet);
        products.add(house);
        products.add(car);

        // Filter filter = new Filter();
        // ArrayList<Product> filteredProductsBySize = filter.filterBySize(products, Size.LARGE);
        // for(Product p : filteredProductsBySize){
        //     System.out.println(p);
        // }

        BetterFilter bFilter = new BetterFilter();
        ColorSpecification colorSpec = new ColorSpecification(Color.RED);
        SizeSpecification sizeSpec = new SizeSpecification(Size.MEDIUM);

        Specification[] specs = {colorSpec, sizeSpec};
        Pattern[] patterns = {Pattern.OR, Pattern.AND};
        ManySpecification manySpec = new ManySpecification(specs, patterns);

        ArrayList<Product> bfilteredProducts = bFilter.filter(products, manySpec);
        for(Product p : bfilteredProducts){
            System.out.println(p);
        }
    }   
}
