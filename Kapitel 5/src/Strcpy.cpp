#include <iostream>
#define m_SIZE 30

void strcpy1(char *s, char *t) {
    int i = 0;
    while(t[i] = s[i])
        i++;
}

void strcpy2(char *s, char *t) {
    while (*t = *s) {
        s++;
        t++;
    }
}

int main() {
    char s[] = "Zeichenketten";
    char t1[m_SIZE], t2[m_SIZE];
    
    strcpy1(s, t1);
    strcpy2(s, t2);

    std::cout << t1 << std::endl;
    std::cout << t2 << std::endl;

    return 0;
}
