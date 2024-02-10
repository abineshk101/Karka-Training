#include <iostream>

class A{
    public:
        int *ptr;
        A(){
            ptr=new int();
            *ptr=10;
        };
        A(const A &obj){
            ptr=new int();
            *ptr=*(obj.ptr);
        };
};

int main(){
    A obj;
    A obj1=obj;
    std::cout << *obj1.ptr;
}