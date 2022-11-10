// #include<iostream>

// using namespace std;

// int main(){
//     string name;
//     int age;
//     cout << "What is your name?" << endl;
//     cin >> name;

//     cout << "How old are you?" << endl;
//     cin >> age;

//     cout << "Hi " << name << endl;
//     cout << "you are " << age << " years old" << endl;   
// }

// #include<iostream>

// using namespace std;

// int main(){
//     string input1;
//     string input2;
//     cin >> input1;
//     cin >> input2;
//     if (input1.size() < input2.size()){
//         cout << "no" << endl;
//     }else{
//         cout << "go" << endl;
//     }
// }

// #include<iostream>
// using namespace std;
// int main(){
//     int count;
//     cin >> count;
//     for (int i = 1; i <= count; i++){
//         cout << i << " Abracadabra" << endl;
//     }
// }
#include<iostream>
using namespace std;
int main(){
    int x;
    int y;
    int n;
    cin >> x >> y >> n;
    for(int i = 1;i <= n; i++){
        if(i % x == 0 and i % y == 0){
            cout << "FizzBuzz" << endl;
        }else if(i % x == 0){
            cout << "Fizz" << endl;
        }else if(i % y == 0){
            cout << "Buzz" << endl;
        }else{
            cout << i << endl;
        }
    }
}