#include <iostream>

using namespace std;

float calcularAreaRectangulo(float base, float altura);

int main() {
    float b, h, resultado;
    char opcion;

    do {
        cout << "--- Calculadora de Area de Rectangulos ---" << endl;
        
        cout << "Introduce la base: ";
        cin >> b;
        
        cout << "Introduce la altura: ";
        cin >> h;

        resultado = calcularAreaRectangulo(b, h);

        cout << "El area del rectangulo es: " << resultado << endl;

        cout << "------------------------------------------" << endl;
        cout << "¿Deseas calcular otra area? (s/n): ";
        cin >> opcion;

    } while (opcion == 's' || opcion == 'S');

    cout << "Programa finalizado." << endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    
    return base * altura;
}