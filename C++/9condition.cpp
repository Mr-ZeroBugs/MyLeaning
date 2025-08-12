#include <iostream>

int main() {
    int age;
    std::cout << "what's ur age: ";
    std::cin >> age;

    if (age>=18) {
        std::cout << "not kid";
    } 
    else if(age < 0) {
        std::cout << "your not human bud";
    }
    else {
        std::cout << "kid";
    }

    // In case it has many cases we can use Switches
    int month;
    std::cout << "month: ";
    std::cin >> month;

    switch (month) {
        case 1:
            std::cout << "Janurty";
            break;
        case 2:
            std::cout << "feb";
            break;
        case 3:
            std::cout << "march";
            break;
        case 4:
            std::cout << "april";
            break;
        default:
            std::cout << "ur month im lazy to write, yeah";
    }
    

    return 0;
}