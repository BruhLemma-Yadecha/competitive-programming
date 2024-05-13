#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <unordered_map>

using namespace std;

unordered_map<int, int> memo;

int count_twos(int x)
{
    // base case: if x is not divisible by 2, return 0
    if (x % 2 != 0) return 0;
    if (memo.count(x)) return memo[x];
    int res = 1 + count_twos(x / 2);
    memo[x] = res;
    return res;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int MOD = pow(2, n);
        int prod = 1;
        for (int i = 0; i < n; i++)
        {
            prod *= a[i];
        }
        if (prod % MOD == 0)
        {
            cout << 0 << endl;
            continue;
        }
        int twos = count_twos(prod);
        vector<int> to_add_twos(n/2);
        for (int i = 1; i < n; i += 2)
        {
            to_add_twos.push_back(count_twos(i + 1));
        }
        int av = accumulate(to_add_twos.begin(), to_add_twos.end(), 0);
        if (twos + av < n)
        {
            cout << -1 << endl;
            continue;
        }
        int target = n - twos;
        sort(to_add_twos.rbegin(), to_add_twos.rend());
        int operations = 0;
        int total = 0;
        for (int num : to_add_twos)
        {
            if (total >= target)
            {
                break;
            }
            total += num;
            operations += 1;
        }
        if (total < target)
        {
            cout << -1 << endl;
            continue;
        }
        cout << operations << endl;
    }
    return 0;
}