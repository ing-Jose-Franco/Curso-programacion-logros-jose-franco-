#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {

    vector<string> comidas;
    string entrada;

    cout << "Introduce 3 de tus comidas favoritas:" << endl;

    for (int i = 0; i < 3; i++) {
        cout << "Comida " << i + 1 << ": ";

        getline(cin >> ws, entrada); 
        comidas.push_back(entrada);
    }

    cout << "\nTu lista de comidas favoritas es:" << endl;
    
    for (const string &comida : comidas) {
        cout << "- " << comida << endl;
    }

    return 0;
}