#include <iostream>
#include <cmath> // to use more math func eg. power

int main() {
    double x = 1;
    double y = 2;
    double z;

    // basic min max func
    z = std::max(x, y);
    std::cout << z << "\n";

    z = std::min(x,y );
    std::cout << z << "\n";

    // math func for cmath include 
    z = pow(2, 4); // 2^4
    z = sqrt(9); //sqareroot
    z = abs(-3); // the absolute |x|
    z = round(3.5); // round is round bruh just round the decimal
    z = ceil(3.1); // 4, always round up
    z =  floor(3.99); // 3, always round down
    
    return 0;
}
