#include <iostream>

int main() 
{
    std::string students[] = {"Ant", "Bee", "Cheetah", "Dog"};

    for (int i=0; i<(sizeof(students)/(sizeof(std::string))); i++) {
        std::cout << students[i] << "\n";
    }

    // for each loop
    for (std::string student : students) {
        std::cout << student << '\n';

    }
}