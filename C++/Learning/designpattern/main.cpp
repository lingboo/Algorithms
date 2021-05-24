#include <vector>
#include <stdio.h>
#include <string>

using namespace std;

enum Color{
    RED, GREEN, BLUE
};

enum Size{
    SMALL, MEDIUM, LARGE
};

class Product{
    string name;
    Color color;
    Size size;

    Product(string _name, Color _color, Size _size){
        name = _name;
        color = _color;
        size = _size;
    }
};

int main(int argc, char const *argv[])
{
    Product p{"Shoes", Color::RED, Size::SMALL};
    return 0;
}

