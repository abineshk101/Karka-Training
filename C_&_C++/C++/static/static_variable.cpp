#include <iostream>

class A{
    public:
        A();
        static int K;
        static int fun1(){
            return A::K=23;
        };
};
int A::K;
int main(){
    A::K=20;
    printf("%d\n",A::K);
    printf("%d",A::fun1());
};