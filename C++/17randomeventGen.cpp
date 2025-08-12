#include <iostream>
#include <ctime>

int main() 
{
    srand(time(NULL));
    int randNum = (rand() % 5) + 1 ;

    switch (randNum) {
        case 1 : std::cout << "You won a t shirt ";
            break;
        case 2 : std::cout << "You won a pants";
            break;
        case 3 : std::cout << "You won a duck";
            break;
        case 4 : std::cout << "You won a paper ";
            break;
        case 5 : std::cout << "You won a trash ";
            break;
    }

    return 0;
}