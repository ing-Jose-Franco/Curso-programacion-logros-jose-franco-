#include <iostream>
#define LIMITE 10

using namespace std;

int main() {
    int numero;

    cout << "Introduce un número para ver su tabla de multiplicar: ";
    cin >> numero;

    cout << "Tabla de multiplicar del " << numero << " (hasta " << LIMITE << "):" << endl;

    for (int i = 1; i <= LIMITE; i++) {
        int resultado = numero * i;
        cout << numero << " x " << i << " = " << resultado << endl;
    }

    return 0;
}