#include "forearmCalc.h"
#include <cmath>

std::tuple<double, double> ForearmCalc::sprocketGeometry(int N, double p) {
    double D = p / (std::sin(M_PI / N));  // Diameter
    double C = M_PI * D;  // Circumference
    return {D, C};
}

int ForearmCalc::stepsForDriverRev(double effectiveSteps) {
    return std::ceil(effectiveSteps);
}

// Implement additional functions based on the Python script's content
