#include <iostream>
#include <cmath>
//A function for newtin sqrt way.
double sqrtnewton(double S, double tolerance = 1e-10) {
    double x = S;
    while (std::abs(x * x - S) > tolerance) {
        x = (x + S / x) / 2.0;
    }
    return x;
}

int main() {
  
}