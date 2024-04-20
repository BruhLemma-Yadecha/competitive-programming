#include <iostream>
#include <set>
#include <string>

using namespace std;

void generate(string st, set<string> &substrings)
{
    if (st.empty())
    {
        return;
    }
    if (substrings.find(st) != substrings.end())
    {
        return;
    }
    substrings.insert(st);
    generate(st.substr(1), substrings);
    if (st.length() > 1)
    {
        generate(st.substr(0, 1) + st.substr(2), substrings);
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        set<string> substrings;
        generate(s, substrings);
        cout << substrings.size() << endl;
    }

    return 0;
}