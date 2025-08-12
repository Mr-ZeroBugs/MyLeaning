#include <iostream>

int main(){
    std::cout << "kuy" << std::endl; // std = standard, cout = character output, << = result, endl = endline, and then ; after the end
    std::cout << "kuy2 (should be in new line because of endl)" << "\n"; // we can use \n instead of endl as well

    int x; // Declaration
    x = 5; // Assignment
    // or
    int y = 6; // Combine
    std::cout << x+y << std::endl;

    // double = float
    double a = 11.5;

    // single character
    char grade = 'A';
    std::cout << grade << std::endl;

    // boolean (true false)
    bool imgay = false;

    // string
    std::string name = "Kongpop";
    std::cout << name << "\n";

    std::cout << "Hello " << name << "\n";

    // in case we dont want to let variable change anymore forever
    int const f = 2;

    return 0;
}