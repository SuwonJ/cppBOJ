#include <iostream>
using namespace std;
int main(void) {
  int n1, n2, n3, max = 0;
  while (1) {
    cin >> n1 >> n2 >> n3;
    if (n1 + n2 + n3 == 0)
      return 0;
    if (n1 * n1 == n2 * n2 + n3 * n3)
      cout << "right\n";
    else if (n2 * n2 == n1 * n1 + n3 * n3)
      cout << "right\n";
    else if (n3 * n3 == n2 * n2 + n1 * n1)
      cout << "right\n";
    else
      cout << "wrong\n";
  }
}
