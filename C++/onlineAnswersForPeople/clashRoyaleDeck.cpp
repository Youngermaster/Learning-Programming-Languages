#include <iostream>

using namespace std;

enum Carta {
    peeka = "peeka",
    minero = "minero"
};

int main(int argc, char const *argv[]) {
    string cart;
    cout << "Cual es tu carta favorita de Clash Royale?: \n";
    cin >> cart;

    if (cart == "pekka") {
        cout << "Muy buena carta\n";
    } else if (cart == "minero") {
        cout << "Buena carta\n";
    } else {
        cout << "No conozco tu carta\n";
    }

    return 0;
}