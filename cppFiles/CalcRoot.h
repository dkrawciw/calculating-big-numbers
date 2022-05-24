#ifndef CALC_ROOT
#define CALC_ROOT

#include <string>

class CalcRoot{
private:
    int initialValue;
    int degree;
    double root;
    double taylorRemainder;

public:
    double DEFAULT_PRECISION = 0.01;

    CalcRoot(int initialValue);
    CalcRoot(int initialValue, double precision);

    int getInitialValue() { return initialValue; }
    double getRoot() { return root; }
    double getAccuracy() { return taylorRemainder; }

    int findCenter(int root, int initialValue);
    double approxRoot(int center);
    double findTaylorRemainder(int center, int nthDegree);

    std::string to_string();
};

#endif