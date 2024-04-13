#ifndef FOREARMCALC_H
#define FOREARMCALC_H

#include <tuple>

class ForearmCalc {
public:
    static std::tuple<double, double> sprocketGeometry(int N, double p);
    static int stepsForDriverRev(double effectiveSteps);
    // Add more functions as necessary, translating the Python functions to C++ methods
};

#endif // FOREARMCALC_H
