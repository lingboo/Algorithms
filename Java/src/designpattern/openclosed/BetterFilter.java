package designpattern.openclosed;

import java.util.ArrayList;

public class BetterFilter {
    
    public ArrayList<Product> filter(ArrayList<Product> products, Specification spec){
        ArrayList<Product> res = new ArrayList<>();
        for(Product p: products){
            if(spec.isSatified(p)){
                res.add(p);
            }
        }
        return res;
    }
}
