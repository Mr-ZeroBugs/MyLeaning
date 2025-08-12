#include <iostream>

void sort(int array[], int size);

int main() 
{
    int array[] = {10, 1, 9, 2, 8, 3, 7, 4, 6, 5};
    int size = sizeof(array)/sizeof(array[0]);

    sort(array, size);

    for (int element : array){
        std::cout << element << " ";
    }

    return 0;
}

void sort(int array[], int size){

    int temp;
    for (int i=0; i < size - 1; i++) { // it's size-1 because we dont need to compare the last element to anything
        for (int j=0; j<size-i-1; j++){ // no need to sort the element that already sorted
            if (array[j] > array[j+1]) {
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}