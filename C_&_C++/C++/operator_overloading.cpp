#include <iostream>

class A{
    public:
        int c;
        int d;
        int x;
        A()
        {
            
        }
        A(int g){
            c=g;
            d=5;
        };
        A operator + (const A &obj){
            A obj2;
            obj2.c=c+d;*
            return obj2;
        };

};

int main(){
    A obj(10);
    A obj1(22.c) ;
}