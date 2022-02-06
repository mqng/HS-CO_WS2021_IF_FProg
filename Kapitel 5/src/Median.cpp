#include <iostream>

#define SWAP(X,Y) {int t=(X); (X) = (Y); (Y) = t;}

using namespace std;

int main() {
    int liste[5];
    cin >> liste[0] >> liste[1] >> liste[2] >> liste[3] >> liste[4];

    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 4; j++) {
            if(liste[j] > liste[j + 1])
                SWAP(liste[j], liste[j + 1]);
        }
    }
    cout << "Median: " << liste[5/2] << endl;
}
