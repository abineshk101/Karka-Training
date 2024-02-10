#include <iostream>

class A{
    public:
        int a;
        int b;
        A(){
            a=10;
        };
        int operator = (const A &obj){
            b=obj.b;
        }
};

int main(){
    A obj;
    A obj2;
    obj2.b=100;
    printf("%d\n",obj.b);
    obj=obj2;
    printf("%d",obj.b);
}