#include <iostream>

int main() {
    std::string name; //declare

    std::cout << "What's ur name? : ";
    std::cin >> name; //this means we let the name variable be the user input
    std::cout << "Hello " << name << "\n"; // btw run this on terminal otherwise you will not be able to type the input when you run the code 

    //but the problem is if we use input and the user type the " " spaces the code will stop reading like "Sty Fa" and it will shows as "Sty"
    //so here is the way to let the code do not skip the spaces
    std::cout << "what the fuck is your name again?: ";
    std::cin.ignore(); // clear the latest input otherwise it will use the old input as value of variable
    std::getline(std::cin, name);   
    // std::getline(std::cin >> std::ws, name); in case you only need to delete white space out of the buffer
    std::cout << name;

    return 0;
}