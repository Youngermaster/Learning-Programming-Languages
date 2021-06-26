#include <iostream>

using namespace std;

void print_intro();

enum Carta {
    peeka,
    minero,
    esqueletos
};

int main(int argc, char const *argv[]) {
    int id_card;
    print_intro();
    cin >> id_card;

    switch (id_card) {
        case peeka:
            cout << "Muy buena carta\n";
            break;
        case minero:
            cout << "Buena carta\n";
            break;
        case esqueletos:
            cout << "Los esqueleto son veloces\n";
            break;
        default:
            cout << "No conozco tu carta :(\n";
            break;
    }

    return 0;
}

void print_intro() {
    cout << "|======================== Bienvenido ========================|" << endl;
    cout << "| Para elegir las cartas digita su ID.                       |" << endl;
    cout << "| Las cartas a elegir son:                                   |" << endl;
    cout << "| Peeka (0)                                                  |" << endl;
    cout << "| Minero (1)                                                 |" << endl;
    cout << "| Esqueleto (2)                                              |" << endl;
    cout << "|                                                            |" << endl;
    cout << "| ¿Cuál es tu carta favorita de Clash Royale?                |" << endl;
    cout << "|============================================================|" << endl;
}