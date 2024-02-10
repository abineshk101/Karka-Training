#include <iostream>

int main(){
    int a=5;
    // int &b=a;
    // std::cout << b;

    int *d=&a;                          //pointer store the address
    std::cout << *d;                    // access the value                                      
    std::cout <<"\n"<< d;                // access the address
}