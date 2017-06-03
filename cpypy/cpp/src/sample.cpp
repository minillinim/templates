#include <iostream>
#include "sample.h"

using namespace std;

void swap(int &x, int &y) {
   x ^= y; // x = xy
   y ^= x; // y = xyy = x
   x ^= y; // x = xxyyy = y
}

int main () {
   // local variable declaration:
   int a = 100;
   int b = 200;

   cout << "Before swap, value of a :" << a << endl;
   cout << "Before swap, value of b :" << b << endl;

   /* calling a function to swap the values using variable reference.*/
   swap(a, b);

   cout << "After swap, value of a :" << a << endl;
   cout << "After swap, value of b :" << b << endl;

   return 0;
}
