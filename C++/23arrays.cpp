#include <iostream>
#include <ctime>

int main()
{
    std::string cars[] = {"Ford", "Mustang", "Honda"}; // arrays can contain a lot data at once but the data gotta be the same data type
    std::cout << cars[0] << '\n';

    std::string cars2[2]; // declare and set a sizd
    cars2[0] = "Car1"; // 
    cars2[1] = "Car2";
    std::cout << cars2[1];
    return 0;

}