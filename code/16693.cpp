#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;
int main(void) {
  long double area, sliceprice, radius, wholeprice;
  cin >> area >> sliceprice >> radius >> wholeprice;
  if ((sliceprice / area) < (wholeprice / (radius * radius * M_PI)))
    cout << "Slice of pizza";
  else
    cout << "Whole pizza";
  return 0;
}
