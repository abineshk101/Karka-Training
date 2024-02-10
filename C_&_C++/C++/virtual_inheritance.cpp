#include <iostream>
using namespace std;

class A
    {
        public:
            A(){
                printf("\nThis id A constructor");
            };
            int classAfun(){
                printf("%s","1A");
            };
            int function2(){
                printf("%s","2A");
            };
            ~A(){
                printf("\nThis id A destructor");
            };
    };

class B:virtual public A
    {
        public:
            B(){
                printf("\nThis id B constructor");
            };
            int classBfun(){
                printf("%s","3B");
            };
            ~B(){
                printf("\nThis id B destructor");
            };
    };

class C:virtual public A
    {
        public:
            C(){
                printf("\nThis id C constructor");
                };
            int classCfun(){
                printf("%s","4C");
            };
            ~C(){
                printf("\nThis id C destructor");
            };
    };

class D:public B,public C
    {
        public:
            D(){
                printf("\nThis id D constructor");
            };
            int classDfun(){
                //C::classAfun();
            };
            ~D(){
                printf("\nThis id D destructor");
            };
    };

int main(){
    // B classB;
    // classB.classBfun();

    D classD;
    classD.classAfun();
};