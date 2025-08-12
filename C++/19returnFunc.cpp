#include <iostream>

double square(double length); // we declared double func becuz we want to return double data type
std::string concatStrings(std::string string1, std::string string2);

int main() 
{
    double length = 5.0;
    double area  = square(length);

    std::string name = "Kongpop";
    std::string Lastname = "Pipatpusit";
    std::string fullname = concatStrings(name, Lastname);

    std::cout << "Area: " << area << "cm^2 \n";
    std::cout << fullname;

    return 0;
}

double square(double length) {
    return length * length;
}

std::string concatStrings(std::string string1, std::string string2) {
    return string1 + " " + string2;
}