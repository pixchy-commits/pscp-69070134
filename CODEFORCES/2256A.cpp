#include<bits/stdc++.h>

using namespace std;

int main(){

    int t;

    cin >> t;

    for (int i = 0; i < t; i++){

        int min = 2e9;
        int max = -2e9;

        int xsum = 0;

        for (int v = 0; v < 3; v++){
            int getN;
            cin >> getN;
            if (getN < min){
                min = getN;
            }

            if (getN > max){
                max = getN;
            }

            xsum += getN;

        }

        int diff = xsum - max;
        int mid = xsum - min - max;

        if (diff > max){
            cout << max - min << "\n";
        } else {
            cout << mid << "\n";
        }

    }
}