#include <iostream>

void swap(std::string &x, std::string &y);

int main()
{
    std::string x = "i am the x";
    std::string y = "i am the y";

    swap(x, y);

    std::cout << "x: " << x << '\n';
    std::cout << "y: " << y << '\n';

    return 0;
}

void swap(std::string &x, std::string &y) { // we use address instead of its value because when it passed to  func it's not the real x it's a copy version
    std::string temp; // so if we dont use address of x, its value won't change 
    temp = x;
    x = y;
    y = temp;
}