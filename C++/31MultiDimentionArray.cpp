#include <iostream>

int main() 
{
    std::string cars[][3] = {{"A", "B", "C"},
                            {"D", "E", "F"},
                            {"G", "H", "I"}}; // x rows 4 columns

    std::cout << cars[1][2];
    int rows = sizeof(cars)/sizeof(cars[0]) ;
    int columns = sizeof(cars[0])/sizeof(cars[0][0]);

    for (int i=0; i<rows; i++) {
        std::cout << "\n";
        for (int j=0; j<columns; j++) {
            std::cout << cars[i][j] << " ";
        }
    }

}