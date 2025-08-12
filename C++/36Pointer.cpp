#include <iostream>

int main()
{
    std::string name = "Bro";
    int age = 21;

    std::string *pName = &name;
    int *pAge = &age;

    std::cout << *pName << "\n";
    std::cout << *pAge;

    return 0;
}