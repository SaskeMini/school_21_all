#include "s21_math.h"

long double s21_fabs(double x) {
  long double result = x;
  if (x < 0) result *= -1;
  return result;
}