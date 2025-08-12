#include <iostream>
#include <ctime>

void HappyBirthday(std::string name, int age); //void means Function that not return anything

int main() 
{
    std::string nameTest = "Bro";
    int age = 21;
    HappyBirthday(nameTest, age); // call function and sent an argument


    return 0;
}

void HappyBirthday(std::string name, int age){ // set up parameter preparing to get argument
    std::cout << "HBD" << name << age; // write the function after the main but we need to declare first at the top
}
