#include <iostream>
using namespace std;

bool is_prime(int num);

int main(){
    long int value = 600851475143;
    long int value_fake = value;
    int found = 0;
    int i=2;
    while (value_fake>1) {
        if(is_prime(i)){
            if (value%i==0) {
                value_fake/=i;
                found = i;
            }
        }
        i++;
    }
    cout << found << "\n";
}

bool is_prime(int num)
{
    if(num==0 or num==1) return false;
    if (num == 2) return true;
    for(int i=2; i<=num/2; i++)
        if(num%i==0)
            return false;
    return true;
}