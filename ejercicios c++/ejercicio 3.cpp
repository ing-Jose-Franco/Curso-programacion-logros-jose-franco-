#include <iostream>
using namespace std;

int main() {
    int edad;

    cout << "Por favor, introduce tu edad: ";
    cin >> edad;

    if (edad >= 18) {
   
        cout << "Eres mayor de edad. Puedes acceder al sistema." << endl;
    } else {
        
        cout << "Eres menor de edad. Acceso restringido." << endl;
    }

    return 0;
}