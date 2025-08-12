#include <iostream>

int main() {
    std::string name;
    while (name.empty()) {
        std::cout << "enter ur name : ";
        std::getline(std::cin, name);
    }

    int num;

    do{ // this is the another version of while loop. the different is it gonna do the block of code first and check condition and then loop and loop at the start once
        std::cout << "enter a positive num : ";
        std::cin >> num;
    }while(num < 0);

    return 0;
}