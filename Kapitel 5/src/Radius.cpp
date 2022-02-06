#include <iostream>

#define m_PI 3.1415927
#define QUAD(X) (X)*(X)
#define CUBE(X) (X)*(X)*(X)

using namespace std;

int main() {
    double r;

    cout << "Radius: ";
    cin >> r;
    cout << "Oberflaeche: " << 4.0 * m_PI * QUAD(r)
        << ", Volumen: " << 4.0/3 * m_PI * CUBE(r) << endl;

    return 0;
}
