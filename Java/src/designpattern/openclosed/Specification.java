package designpattern.openclosed;

public interface Specification {
    boolean isSatified(Product product);
}

class ManySpecification implements Specification{
    Specification[] specs;
    Pattern[] patterns;

    @Override
    public boolean isSatified(Product product) {
        boolean res = false;
        boolean triggerAnd;

        for(int i=0; i<this.patterns.length; i++){
            if(patterns[i] == Pattern.AND){
                triggerAnd = true;
                res = (res || triggerAnd) && (specs[i].isSatified(product) && specs[i+1].isSatified(product));
            }else{
                res = res || (specs[i].isSatified(product) || specs[i+1].isSatified(product));
            }
        }
        return res;
    }

    public ManySpecification(Specification[] specs, Pattern[] patterns){
        if(specs.length != patterns.length+1){
            throw new ArrayIndexOutOfBoundsException("Patterns should be length of specs -1");
        }
        this.specs = specs;
        this.patterns = patterns;
    }
}

class ColorSpecification implements Specification{
    private Color color;

    @Override
    public boolean isSatified(Product product) {
        return product.color == this.color;
    }

    public ColorSpecification(Color color){
        this.color = color;
    }
}

class SizeSpecification implements Specification{
    private Size size;

    @Override
    public boolean isSatified(Product product) {
        return product.size == this.size;
    }

    public SizeSpecification(Size size){
        this.size = size;
    }
}