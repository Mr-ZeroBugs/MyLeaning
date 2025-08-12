#include <iostream>
#include <ctime>

char getUserChoice();
char getComputerChoice();
void showChoice(char choice);
void chooseWinner(char player, char computer);

int main() 
{
    char player;
    char computer;

    player = getUserChoice();
    std::cout << "your choice :";
    showChoice(player);

    computer = getComputerChoice(); 
    std::cout << "Computer's choice : ";
    showChoice(computer);

    chooseWinner(player, computer);

    return 0;
}
///

char getUserChoice() {

    char player;
    std::cout << "Rock-Paper-Scissors Game!\n";
    std::cout << "choose one!\n";
    std::cout << "******************\n";
    
    do {
        std::cout << "r for rock\n";
        std::cout << "p for paper\n";
        std::cout << "s for scissor\n";
        std::cin >> player;
    }while (player != 'r' && player!= 'p' && player != 's');
    return player;
}

char getComputerChoice() {
   srand(time(0)); 
   int num = rand() % 3 + 1;

   switch(num) {
        case 1 : return 'r';
        case 2 : return 'p';
        case 3 : return 's';
   }
}

void showChoice(char choice) {
    switch (choice){
        case 'r' : std::cout << "rock\n";
            break;
        case 'p' : std::cout << "paper\n";
            break;
        case 's' : std::cout << "scissor\n";
            break;
    }

}

void chooseWinner(char player, char computer) {
    switch(player) {
        case 'r' : if(computer == 'r'){
            std::cout << "it's a tie!\n";
        } else if (computer == 'p') {
            std::cout << "you lose!\n";
        } else {
            std::cout << "you win!\n";
        }
        break;

        case 'p' : if(computer == 'p'){
            std::cout << "it's a tie!\n";
        } else if (computer == 's') {
            std::cout << "you lose!\n";
        } else {
            std::cout << "you win!\n";
        }
        break;

        case 's' : if(computer == 's'){
            std::cout << "it's a tie!\n";
        } else if (computer == 'r') {
            std::cout << "you lose!\n";
        } else {
            std::cout << "you win!\n";
        }
        break;
    }
}