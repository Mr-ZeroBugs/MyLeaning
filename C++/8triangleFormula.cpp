#include <iostream>
#include <cmath>

int main() { 
    double a;
    double b;
    double c;

    std::cout << "What's the A: ";
    std::cin >> a ;

    std::cout << "what's the b: ";
    std::cin >> b;

    c = sqrt(pow(a, 2) + pow(b, 2));
    std::cout << "the answer C is " <<  c;
    
    return 0;
}