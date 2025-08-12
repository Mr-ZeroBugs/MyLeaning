#include <iostream>

int main() 
{
    // sizof () Is the func that shows the size in bytes of a variable

    std::string name = "bro"; // even if string variable has 1 char like a char data type it still be 32 bytes 
    double gpa = 2.5;
    char grade = 'f';
    bool student = false;
    char grades[] = {'F', 'C', 'B', 'A'};

    std::cout << sizeof(gpa) << "bytes\n"; // 8 bytes for double
    std::cout << sizeof(name) << "bytes\n"; // 32 bytes for string
    std::cout << sizeof(grade) << "bytes\n"; // 1 b for char
    std::cout << sizeof(student) << "bytes\n"; // 1 b for bool
    std::cout << sizeof(grades) << "bytes\n"; // size of array's type * num of value in array = total size (1*4 = 4)
    std::cout << "total elements : " << sizeof(grades)/sizeof(char);

    return 0;
}