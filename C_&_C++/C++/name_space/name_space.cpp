#include <iostream>
# include "class1.h"
#include "class2.h"

using namespace sample2;
int main(){
    printf("%d\n",a);

    sample1::A obj ;
    obj.fun1();

    sample2::A obj1;
    obj1.fun1();
}

// using namespace sample2;
// int main(){
//     printf("%d\n",a);
// }

