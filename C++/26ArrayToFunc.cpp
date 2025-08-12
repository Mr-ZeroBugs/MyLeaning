#include <iostream>

double Sum(double prices[], double size);

int main() 
{
    double prices[] = {49.99, 15.05, 75, 9.99};
    double size = sizeof(prices)/sizeof(prices[0]);
    double total = Sum(prices, size);

    std::cout << "sum : " << total;
}

double Sum(double prices[], double size) {
    double total = 0;

    for (int i=0; i < size; i++) {
        total = total + prices[i];
    }

    return total;
}