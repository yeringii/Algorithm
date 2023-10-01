#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long long check = sqrt(n);
    if(check*check == n)answer=pow(check+1, 2);
    else answer = -1;
    return answer;
}