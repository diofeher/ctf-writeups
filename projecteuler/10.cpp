#include <iostream>
using namespace std;

bool is_prime(int num);

int main()
{
    unsigned long long int sum = 0;
    for(long int i=2; i<2000000; i++)
        if (is_prime(i)) {
            sum += i;
            cout << sum << "\n";
        }
    cout << sum << "\n";
}

bool is_prime(int num)
{
    for(int i=2; i<num/2+1; i++)
        if(num%i==0)
            return false;
    return true;
}