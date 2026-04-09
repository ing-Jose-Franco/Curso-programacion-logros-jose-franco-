int main() {
    // Definimos el PIN inicial (en una app real esto sería dinámico)
    CajaFuerte miCaja(1234);
    int intento;
    bool exito = false;

    cout << "--- CAJA FUERTE ELECTRONICA ---" << endl;

    // Bucle do-while que solicita el PIN al menos una vez
    do {
        cout << "Introduce el PIN secreto: ";
        cin >> intento;

        exito = miCaja.intentarAbrir(intento);

        if (!exito) {
            cout << "PIN incorrecto. Intenta de nuevo." << endl;
        }

    } while (!exito);

    cout << "Acceso concedido. La caja fuerte se ha abierto." << endl;

    return 0;
}