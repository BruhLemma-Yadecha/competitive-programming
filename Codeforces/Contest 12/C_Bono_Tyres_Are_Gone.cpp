#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int next_tyre = 1;
    vector<int> pile;
    int shufflings = 0;
    for (int i = 0; i < 2 * n; ++i)
    {
        string command;
        cin >> command;
        if (command == "add")
        {
            int tyre;
            cin >> tyre;
            pile.push_back(tyre);
        }
        else
        {
            if (next_tyre != pile.back())
            {
                sort(pile.rbegin(), pile.rend());
                ++shufflings;
            }
            pile.pop_back();
            ++next_tyre;
        }
    }
    cout << shufflings << endl;
    return 0;
}