#include <iostream>

template <typename T,typename Y>
class A{
    public:

        Y fun1(T a,Y b){
            return a+b;
        };
};

int main(){
    A <int,float> obj;
    printf("%f",obj.fun1(1.1,2.1));
}