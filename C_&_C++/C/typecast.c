#include <stdio.h>

//*******Implicit typecast ***********//

// int main(){
//     int a=5;
//     int b=2;
//     float c;
//     c=a/b;
//     printf("%f",c);
// };

//*******Explicit typecast ***********//

int main(){
    int a=5.2;
    int b=2;
    int c;
    c=(float)a /b;
    printf("%d",c);
}