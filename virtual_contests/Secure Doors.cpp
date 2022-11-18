#include <map>
#include <iostream>
using namespace std;
int main()
{
    int count;
    cin >> count;
    map<string, string> m;

    for (int i = 1; i <= count; i++)
    {
        string status, name;
        cin >> status >> name;
        if (status == "entry" and m.find(name) == m.end())
        {   
            m[name] = status;
            cout << name << " entered" << endl;
        }
        else if (status == "exit" and m.find(name) != m.end())
        {   
            m.erase(name);
            cout << name << " exited" << endl;
        }
        else if (status == "exit" and m.find(name) == m.end())
        {   
            cout << name << " exited (ANOMALY)" << endl;
        }
        else if (status == "entry" and m.find(name) != m.end())
        {   
            cout << name << " entered (ANOMALY)" << endl;
        }
    }
}