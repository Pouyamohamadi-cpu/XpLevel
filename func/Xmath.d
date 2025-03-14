import std.math;

extern (C) int absvalue(int a) {
    return abs(a);
}

extern (C) double arcSinh(double b) { // تغییر نوع بازگشتی به double
    return asinh(b);
}

extern (C) double acoSinh(double v) { // تغییر نوع بازگشتی به double
    return acosh(v);
}

extern (C) double ataSinh(double letif) { // تغییر نوع بازگشتی به double
    return atanh(letif);
}

extern (C) double lfactorial(int n) { // تغییر نوع ورودی به int و نوع بازگشتی به double
    double result = 0.0;
    for (int i = 1; i <= n; i++) {
        result += log(i);
    }
    return result;
}