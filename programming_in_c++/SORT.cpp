// #include <iostream>
// #include <vector>
#include <bits/stdc++.h>
using namespace std;
// variables
int main()
{
    // vector<int> v  = {4,2,5,3,5,8,3};
    // sort(v.begin(),v.end());
    // for(auto i: v){
    //     cout << i << " ";
    // }
    int n = 7; // array size    
    int a[] = {4,2,5,3,5,8,3};
    sort(a,a+n);

    int k = 0;
    int x = 4;
    for (int b = n/2; b >= 1; b /= 2) {
        while (k+b < n && a[k+b] <= x) {
            k += b;
            cout << b << k << "\n";
        }
        if (a[k] == x) {
        // x found at index k
            cout << k << "\n";
        }
    }
    // for(auto i: a){
    //     cout << i << "\n";
    // }
    // cout << (15 / 5) << endl;
    // cout << (2 / 2) << endl;
    // cout << (7 / 2) << endl;
    // cout << (-7 / 2) << endl;
    // cout << (7 / -2) << endl;
    // Print Hello World!
    // cout << "a pritty hei!" << endl;
}