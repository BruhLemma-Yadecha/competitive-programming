#include <iostream>
#include <vector>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    vector<int> result;

    for(int i = 0; i < cases; i++) {
        int subcases;
        cin >> subcases;

        int bottom = 0;
        int top = 2147483647;
        vector<int> blacklist;

        for(int j = 0; j < subcases; j++){
            int constraint, value;
            cin >> constraint >> value;
            if (constraint == 1) {
                bottom = max(bottom, value);
            } else if (constraint == 2) {
                top = min(top, value);
            } else {
                blacklist.push_back(value);
            }
        }

        int excluded = 0;
        for (int i : blacklist) {
            if (i >= bottom && i <= top)
                excluded++;
        }

        result.push_back(max(top - bottom - excluded + 1, 0));
    }

    for (int i : result) {
        cout << i << endl;
    }
}