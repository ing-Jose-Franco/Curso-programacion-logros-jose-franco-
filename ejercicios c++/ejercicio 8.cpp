#include <iostream>

using namespace std;


void modificarPorValor(int n) {
    n += 10;
    cout << "[Dentro de modificarPorValor]: " << n << endl;
}

void modificarPorReferencia(int &n) {
    n += 10;
    cout << "[Dentro de modificarPorReferencia]: " << n << endl;
}

int main() {
    int numero = 20;

    cout << "Valor inicial: " << numero << endl;

    modificarPorValor(numero);
    cout << "Valor tras modificarPorValor: " << numero << " (No cambio)" << endl;

    cout << "-----------------------" << endl;

    modificarPorReferencia(numero);
    cout << "Valor tras modificarPorReferencia: " << numero << " (Si cambio)" << endl;

    return 0;
}