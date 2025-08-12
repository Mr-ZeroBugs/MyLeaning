#include <iostream>

int main() {
    std::string name = "Test";
    
    std::cout << name.length() << "\n"; // show a length of the text

    name.clear(); // delete the value of variable
    std::cout << "hi " << name << "\n"; 

    if (name.empty()) { // check the value that empty or not
        std::cout << "plz enter the name" << "\n";
    }

    name = "nigke";
    std::cout << name.append("@gmail.com") << "\n";

    std::cout << name.at(0) << "\n"; // the first index
    std::cout << name.insert(0, "Mr") << "\n"; // insert the word you want to the index you want (it also added forver)
    std::cout << name.find('n') << "\n"; // n is in index 2 Mrn
    std::cout << name.erase(0, 2); // delete the word (first index to ... index - 1)


    return 0;
}