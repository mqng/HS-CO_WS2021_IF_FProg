#include <iostream>

int main() {
    int n = 3;
    float a = 0, b = 3.2;
    int m;
    char c, e = 1;

    m = (n % 2) ? (-1 + n) : n;
    std::cout << m << std::endl;

    a = (1/2) * b;
    std::cout << a << std::endl;

    c = 4 < (1 << n);
    std::cout << (int)c << std::endl;

    c = ((1 / e) / b) + a;
    std::cout << (int)c << std::endl;
}
