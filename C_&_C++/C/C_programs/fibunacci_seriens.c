#include <stdio.h>

int main(){
    int first_num=0;
    int second_num=1;
    int fib_num;
    
    int new_num=first_num+second_num;
    
    printf("Enter a number: ");
    scanf("%d",&fib_num);
    
    if(fib_num==0){
        printf("%d",first_num);
    }else if(fib_num==1){
      printf("%d",second_num);  
    }else{
    printf("%d\n%d",first_num,second_num);
    for(int i=3;i<=fib_num;i++){
        printf("\n%d",new_num);
        first_num=second_num;
        second_num=new_num;
        new_num=first_num+second_num;
    }
    }
}