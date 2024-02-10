#include <iostream>

template <typename T,typename Y>
    T fun(T a,Y b){
        return a+b;
    };

int main(){
    std::cout << fun<float>(1,2.1);
}