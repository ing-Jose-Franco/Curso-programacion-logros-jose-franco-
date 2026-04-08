#include <iostream>

using namespace std;

int main() {
    int numeroSecreto = 42;
    int intento;

    cout << "¡Bienvenido al juego de adivinanza!" << endl;
    cout << "He pensado un número. ¿Puedes adivinar cuál es?" << endl;

    cout << "Introduce tu número: ";
    cin >> intento;

    while (intento != numeroSecreto) {
        if (intento < numeroSecreto) {
            cout << "Pista: El número secreto es MÁS ALTO." << endl;
        } else {
            cout << "Pista: El número secreto es MÁS BAJO." << endl;
        }

        cout << "Inténtalo de nuevo: ";
        cin >> intento;
    }

    cout << "¡Felicidades! Has adivinado el número: " << numeroSecreto << endl;

    return 0;
}