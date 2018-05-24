#include <iostream>
#include <math.h>
using namespace std;

// TODO : IT LOOKS I CAN'T SOLVE 48 WITH PROGRAMMING

int main() {
    int num=100;
    unsigned long long int sum=0;
    for(int i=1; i<=num; i++) {
        cout << sum << "\n";
        sum += pow(i, i);
    }
}