#include <iostream>
#include <string>

std::string strToUpperA(const std::string& s1) {
    std::string s2;
    s2 = " ";

    for(int i = 0; i < s1.length(); i++)
        s2+= toupper(s1[i]);
    return s2;
}

int main() {
    std::string s1 = "coburg";
    std::string s3 = strToUpperA(s1);
    std::cout << s3 << std::endl;
    return 0;
}
