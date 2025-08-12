#include <iostream>

int main() 
{
    for (int i = 1; i<=20; i++){
        if (i==13) {
            continue; // skip and continue
        } else if (i==19) {
            break; //stop the loop
        }
        std::cout << i << '\n';
    }

    return 0;
}