#include <iostream>

int main() 
{
    int size = 10;
    std::string foods[size];

    fill(foods, foods+(size/2), "pizza "); // fill the first half with pizza
    fill(foods+(size/2), foods+size, "hamburger "); //fill the second half with hamburger foods+(size/2) refers to second half

    for (std::string food : foods) {
        std::cout << food;
    } 
}