package designpattern.openclosed;

import java.util.ArrayList;

//This is bad whenever we want add a new filter we have to duplicate the code.
public class Filter {
    
    public ArrayList<Product> filterBySize(ArrayList<Product> products, Size size){
        ArrayList<Product> res = new ArrayList<>();
        for(Product p: products){
            if(p.size ==  size){
                res.add(p);
            }
        }
        return res;
    }

    public ArrayList<Product> filterByColor(ArrayList<Product> products, Color color){
        ArrayList<Product> res = new ArrayList<>();
        for(Product p: products){
            if(p.color ==  color){
                res.add(p);
            }
        }
        return res;
    }

    public ArrayList<Product> filterBySizeAndColor(ArrayList<Product> products, Size size, Color color){
        ArrayList<Product> res = new ArrayList<>();
        for(Product p: products){
            if(p.size ==  size && p.color == color){
                res.add(p);
            }
        }
        return res;
    }
}
