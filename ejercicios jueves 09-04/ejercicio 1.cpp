#include <iostream>
using namespace std;

class TanqueAgua {
private:
    double capacidadMaxima;
    double nivelActual;

public:

    TanqueAgua(double capacidad) {
        capacidadMaxima = capacidad;
        nivelActual = 0;
    }

    double getNivel() { return nivelActual; }
    double getCapacidad() { return capacidadMaxima; }

    void llenarTanque(double flujo) {
        if (nivelActual + flujo > capacidadMaxima) {
            nivelActual = capacidadMaxima;
        } else {
            nivelActual += flujo;
        }
    }
};

int main() {

    TanqueAgua miTanque(100.0);
    double flujoEntrada = 12.5;

    while (miTanque.getNivel() < miTanque.getCapacidad()) {
        miTanque.llenarTanque(flujoEntrada);
        
        cout << "Llenando... Nivel actual: " << miTanque.getNivel() << endl;
    }

    cout << "Tanque lleno al maximo." << endl;

    return 0;
}