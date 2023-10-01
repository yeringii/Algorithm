#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string temp = to_string(n);
    
    sort(temp.begin(), temp.end(), greater<>());
    
    answer = stoll(temp);
    
    return answer;
}