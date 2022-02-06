#include <iostream>

int main() {
    int a=10, b, c;
    a*=5+10;
    std::cout << a << std::endl;
    a*=b=c=20;
    std::cout << a << ", " << b << std::endl;
    b=b==c;
    std::cout << b << std::endl;
    a >>= b + 2;
    std::cout << a << std::endl;
    a&= 0x3e;
    std::cout << a << std::endl;

    a=3;
    b=2;
    a*=b+=a<<a+b;
    std::cout << "a= "<< a <<", b= " <<  b << std::endl;
}
