#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

unordered_set<int> binary_decimals;

void generate(int n, vector<int> ls)
{
    if (n == 0)
    {
        int num = 0;
        for (int i = 0; i < ls.size(); i++)
        {
            num = num * 10 + ls[i];
        }
        binary_decimals.insert(num);
        return;
    }
    ls.push_back(0);
    generate(n - 1, ls);
    ls.back() = 1;
    generate(n - 1, ls);
}

bool find_combination(int n)
{
    if (n == 1)
    {
        return true;
    }
    for (auto option : binary_decimals)
    {
        if (n % option == 0 && find_combination(n / option))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    generate(4, {});
    binary_decimals.erase(std::remove(binary_decimals.begin(), binary_decimals.end(), 0), binary_decimals.end());
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        if (find_combination(n))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}