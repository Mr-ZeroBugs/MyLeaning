#include <iostream>

int getDigit(const int number);
int sumOddDigits(const std::string cardNumber);
int sumEvenDigits(const std::string cardNumber);

int main() 
{
    std::string cardNumber;
    int result = 0;

    std::cout << "Enter a credit card : ";
    std::cin >> cardNumber; 

    result = sumEvenDigits(cardNumber) + sumOddDigits(cardNumber);
    if (result % 10 == 0) {
        std::cout << "valid";
    } else {
        std::cout << "fraud";
    }
    std::cout << 1/10%10;

    return 0;

}

int getDigit(const int number){
    // 18       8               1 
    return number % 10 + (number / 10 % 10);
}

int sumEvenDigits(const std::string cardNumber) {
    int sum = 0;

    for (int i = cardNumber.size() - 2; i >= 0; i-=2) {
        sum += getDigit((cardNumber[i] - '0')* 2); // ตรงนี้ cardNumber[i] (char) - '0' (char) ทำให้มันเเปลงเป็นเลข ascii อัตโนมัติ อย่าง 1 = 49, 0=48, 49-48=1 return ตัวเลข int จริงกลับมา
    }

    return sum;
}

int sumOddDigits(const std::string cardNumber) {
    int sum = 0;

    for (int i = cardNumber.size() - 1; i >= 0; i-=2) {
        sum += getDigit(cardNumber[i] - '0');
    }

    return sum;
}