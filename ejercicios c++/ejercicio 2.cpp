#include <iostream>
#include <cmath>

using namespace std;

int main() {
    
    double num1, num2;

    cout << "--- Calculadora C++ con cmath ---" << endl;
    cout << "Introduce el primer numero: ";
    cin >> num1;
    cout << "Introduce el segundo numero: ";
    cin >> num2;

    cout << "\n--- Operaciones Basicas ---" << endl;
    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicacion: " << num1 * num2 << endl;
    
    if (num2 != 0) {
        cout << "Division: " << num1 / num2 << endl;
    } else {
        cout << "Division: No se puede dividir por cero." << endl;
    }

    cout << "\n--- Operaciones con <cmath> ---" << endl;
    cout << "Potencia (" << num1 << "^" << num2 << "): " << pow(num1, num2) << endl;
    
    if (num1 >= 0) {
        cout << "Raiz cuadrada de " << num1 << ": " << sqrt(num1) << endl;
    } else {
        cout << "Raiz cuadrada: No definida para numeros negativos en el conjunto real." << endl;
    }

    return 0;
}