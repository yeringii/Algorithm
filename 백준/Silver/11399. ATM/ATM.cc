#include <iostream>
#include <algorithm>
#include <vector>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n, p;
    int time = 0;

    cin >> n;
    vector<int> v; 
    for(int i = 0; i < n; i++){
        cin >> p;
        v.push_back(p);
    }

    //오름 차순 정렬
    sort(v.begin(), v.end());

    for(int i=0; i < v.size(); i++){
        for(int j=0; j <= i; j++){
            time += v[j];
            //cout << time << endl;
        }
    }
    cout << time;
}