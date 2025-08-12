#include <iostream>

int searchArray(int numbers[], int size, int myNum);

int main() 
{
    int numbers[] = {1, 2, 3, 4, 5, 6, 7 ,8, 9, 10};
    int size = sizeof(numbers)/sizeof(numbers[0]);
    int index;
    int myNum;

    std::cout << "choose the number 1-10 : ";
    std::cin >> myNum;

    index = searchArray(numbers, size, myNum);
    std::cout << index;

    return 0;
}


int searchArray(int numbers[], int size, int myNum) {

    for (int i=0; i<size; i++) {
       if (numbers[i] == myNum) {
        return i;
       }
    }
    return -1;
}