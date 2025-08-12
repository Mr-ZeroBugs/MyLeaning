#include <iostream>

int main() 
{
    std::string name = "Bro";
    int age = 21;
    bool student = true;

    std::cout << &name; // we use & in front of the variable to show its address
}