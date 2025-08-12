#include <iostream>

int main() {
    int grade = 2;

    grade >= 60 ? std::cout << "you pass" : std::cout << "ur not pass" << "\n";
    //this is the short version of if else which is "Structure = Condition ? True case : false case;"

    //here is the simple case to understand 
    bool hungry = false;
    std::cout << "are you hungry" << "\n";
    hungry ? std::cout << "yes" : std::cout << "no"; 
    // or 
    std::cout << (hungry ? "yes hungry" : "nah ur not hungry");

    return 0;
}