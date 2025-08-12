#include <iostream>

// these are like the different universe it's seperated from each others until we refer to them
namespace first{
    int x = 1;
}

namespace second{
    int x = 2;
}

int main() {
    int x = 0;
    
    std::cout << x << "\n"; //0

    std::cout << first::x << "\n"; // 1

    std::cout << second::x << "\n"; // 2
     
    using namespace first; //call it at once and anything after this line will be connected to namepace "first"
    std::cout << x;

    

    return 0;
}
