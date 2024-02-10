#include <iostream>

class A
    {
        public:
            int classAfun(){
                printf("%s","1A");
            };
            int function2(){
                printf("%s","2A");
            };
    };

class B:public A
    {
        public:

            int classBfun(){
                printf("%s","3B");
            };
    };

class C:public B
    {
        public:
            int classCfun(){
                printf("%s","4C");
            };
    };


int main(){
    // C* ptr=new C();
    // ptr->classAfun();
    // ptr->classBfun();
    // ptr->classCfun();
    B* ptr=new B();
    ptr->classBfun();
    ptr->classAfun();
    // A* ptr=new C();
    // ptr->classAfun();
}