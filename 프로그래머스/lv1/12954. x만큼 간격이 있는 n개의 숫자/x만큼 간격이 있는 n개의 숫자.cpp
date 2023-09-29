#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int target = x;
    for(int i = 0; i < n ; i++){
        answer.push_back(target);
        target += x;
    }
    return answer;
}