#include <iostream>

int main() {
    int correct =  8;
    int question = 10;
    double score =  correct/question;

    std::cout << score << "% \n"; // it'll be zero because int correct / question is 0.8 but it cuts out the decimal so it's 0

    score =  (double)correct/question; // here is  the way to fix just add double in front of it to turn it to double type (you can add (double to either correct or question))
    std::cout << score;

    return 0;
}
