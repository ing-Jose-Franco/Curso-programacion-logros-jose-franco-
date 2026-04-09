#include <iostream>

using namespace std;

int main() {
    int opcion;

    do {
  
        cout << "\n--- MENÚ DE OPCIONES ---" << endl;
        cout << "1. Saludar" << endl;
        cout << "2. Despedirse" << endl;
        cout << "3. Salir" << endl;
        cout << "Seleccione una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "¡Hola! Espero que tengas un excelente día." << endl;
                break;
            case 2:
                cout << "¡Adiós! Que te vaya muy bien." << endl;
                break;
            case 3:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Opción no válida. Por favor, intenta de nuevo." << endl;
                break;
        }

    } while (opcion != 3);

    return 0;
}