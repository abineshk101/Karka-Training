#include <iostream>
using namespace std;

int main(){
    int first_num=0;
    int second_num=1;
    int n;
    cout<<"Enter the number";
    cin>>n;
    int new_num=first_num+second_num;
    if(n==0){
        cout<<0;
    }else if(n==1){
        cout<<1;
    }else{
        cout<<0<<"\n"<<1;
        for(int i=3;i<=n;i++){
            cout<<'\n'<<new_num;
            first_num=second_num;
            second_num=new_num;
            new_num=first_num+second_num;

        };
    };
}