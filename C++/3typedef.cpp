#include <iostream>
#include <vector>

typedef std::string text_t;
typedef int number_t; // these are like use Variable instead of typing the whole command

using text_t = std::string;
using number_t = int;
// we can just use Using keyword and it's kinda better to read for me

int main(){
    text_t firstname = "Bro";
    std::cout << firstname << "\n";

    number_t age = 15;
    std::cout << age << "\n";

    return 0;
}