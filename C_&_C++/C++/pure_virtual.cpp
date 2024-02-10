#include <iostream>

class A{
    public:
        virtual int fun()=0;
        void fun3(){
            printf("hello void");
        }
};

class B:public A{
    public:
        int a=10;
        virtual int fun(){
            fun3();
        }
};

int main(){
    // B obj;
    // obj.fun3();
    A* ptr=new B();
    int var=1;
    switch(var){
        case 1:
            ptr->fun();
            break;
    };
    // ptr->fun();
}