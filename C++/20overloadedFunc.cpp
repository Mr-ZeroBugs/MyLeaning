#include <iostream>

void bakepizza();
void bakepizza(std::string topping);

int main() {
    bakepizza();
    bakepizza("macoroni"); // it means func can share the name together if the parameters is different


    return 0;
}

void bakepizza() {
    std::cout << "here's ur pizza";
}

void bakepizza(std::string pizza) {
    std::cout << "here's ur pizza with " + pizza;
}

