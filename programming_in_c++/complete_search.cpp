
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n = 3;
    cout << (1 << n); 
    for (int b = 0; b < (1 << n); b++)
    {
        vector<int> subset;
        for (int i = 0; i < n; i++)
        {
            if (b & (1 << i))
                // cout << "res" << b << "hey" << i << "i" << (1 << i);
                subset.push_back(i);
        }
        for(auto i:subset){
            cout << i;
        }
        cout << "\n";
    }
}

// void search(int k)
// {
//     vector<int> subset;
//     if (k == 3)
//     {
//         // process subset
//         for (auto i : subset)
//         {
//             cout << i << "h";
//         }
//         cout << "\n";
//     }
//     else
//     {
//         search(k + 1);
//         subset.push_back(k);
//         search(k + 1);
//         subset.pop_back();
//     }
// }
// int main()
// {
//     int n = 3;
//     search(0);
// }

