#include<bits/stdc++.h>
#include<vector>
using namespace std;

int main(){
    int t;
    cin >> t;

    while (t--){
        vector<long long> a(3);
        cin >> a[0] >> a[1] >> a[2];

        sort(a.begin(),a.end());

        int min_range = min(a[2]-a[0],a[1]);
        cout << min_range << "\n";
    }
}