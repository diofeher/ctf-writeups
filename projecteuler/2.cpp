#include <iostream>
using namespace std;

int LIMIT = 4000000;

int main(){
    int a=0;
    int b=1;
    int sum=0;
    while (b < LIMIT) {
        int c = a;
        a = b;
        b = c + b;
        if (b % 2==0)
            sum += b;
    }
    printf("%d\n", sum);
}