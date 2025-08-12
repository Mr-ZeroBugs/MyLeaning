#include <iostream>
#include <ctime>

int main() 
{
    srand(time(NULL));

    // random num 1-6 3 times
    int num1 = (rand() % 6) + 1;
    int num2 = (rand() % 6) + 1;
    int num3 = (rand() % 6) + 1;

    // show the num 
    std::cout << num1 << '\n';
    std::cout << num2 << '\n';
    std::cout << num3 << '\n';


    return 0;
}