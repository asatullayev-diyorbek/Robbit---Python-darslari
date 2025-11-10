#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, y;
    double a = 5;
    double b = 4;

    cout << "x ni kiriting: ";
    cin >> x;

    if (x > 0.8) {
        y = pow(2.6, log(x)) - sin(sqrt(x));
    }
    else if (fabs(x - 0.8) < 1e-9) { // x == 0.8
        y = pow(a, 2 * x - sqrt(b)) - acos(x);
    }
    else { // x < 0.8
        y = cos(2 * x) + fabs(x - a - b);
    }

    cout << "y = " << y << endl;

    return 0;
}
