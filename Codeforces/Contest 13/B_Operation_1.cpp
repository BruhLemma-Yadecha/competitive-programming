#include <iostream>

int main()
{
    int a, m;
    std::cin >> a >> m;
    int twos = a / 2;
    a -= twos * 2;
    int ones = a;
    a = 0;
    while ((ones + twos) % m != 0 && twos > 0)
    {
        twos -= 1;
        ones += 2;
    }
    if ((ones + twos) % m == 0)
    {
        std::cout << (ones + twos);
    }
    else
    {
        std::cout << -1;
    }
    return 0;
}