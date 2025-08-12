#include <iostream>

int myNum = 3;

int main() 
{
    int myNum = 2;
    std::cout << ::myNum; // the result will be 3 because we use :: which refers to global variable instead of local
}