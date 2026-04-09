#include <iostream>

using namespace std;


const double PI = 3.14159;


void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    cout << "El perimetro del circulo con radio " << radio << " es: " << perimetro << endl;
}

int main() {
    double radioUsuario;

    cout << "--- Calculo de Perimetro ---" << endl;
    cout << "Introduce el radio del circulo: ";
    cin >> radioUsuario;

    calcularPerimetro(radioUsuario);

    return 0;
}