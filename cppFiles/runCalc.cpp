#include <iostream>

using namespace std;

int main(){
    char ans = ' ';
    bool runLoop = true;

    cout << "Big-Number Calculator" << endl;
    cout << "Choose an option below (or enter q to quit):\n---------------------\n1) Root Calculator\n---------------------" << endl;
    
    while (runLoop){
        cout << "> ";
        cin >> ans;
        ans = tolower(ans);

        switch (ans){
            case '1':
                cout << "You chose the root calculator" << endl;
                break;
            case 'q':
                cout << "Ok, bye!" << endl;
                runLoop = false;
                break;
            default:
                cout << "Invalid Option, try again!" << endl;
                break;
        }
    }

    return 0;
}