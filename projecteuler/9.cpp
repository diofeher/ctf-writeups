#include <iostream>
#include <math.h>

using namespace std;

bool is_pythagorean(int a, int b, int c);

int main(){
// TODO FIX THIS DUMB WAY AND BRUTAL FORCE :(
    for(int x=100; x<500; x++) {
        for(int y=x; y<500; y++)
            for(int z=y; z<500; z++)
                if (is_pythagorean(x,y,z))
                    if (x+y+z ==1000) {
                        cout << x*y*z << "\n";
                        break;
                    }
    }
}

bool is_pythagorean(int a, int b, int c) {
    return pow(a, 2) + pow(b, 2)==pow(c,2);
}