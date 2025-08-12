#include <iostream>

int main(){
    int students = 20;

    students = students + 1;
    std::cout << students << "\n";

    students += 1; // better version it definitely easier
    std::cout << students << "\n";

    students++; // work as well and mostly seen in loop but only + and - can use
    std::cout << students; 

    return 0;
}