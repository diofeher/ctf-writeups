#include <iostream>
using namespace std;

bool can_divide_all(int number, int value);

int main()
{
    int i=0;
    while (1) {
        i++;
        bool found = can_divide_all(i,20);
        if (found) {
            std::cout << i << "\n";
            break;
        }
    }
}

bool can_divide_all(int number, int value)
{
    int sum=0;
    for(int i=1; i<=value; i++)
        if (number%i==0) 
            sum ++;
            
    return (sum == value);
}