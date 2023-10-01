#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(int n) {
    bool answer = false;
    int x = n;
    int sum = 0;
    while (n > 0){
        sum += n % 10;
        n /= 10;
    }
    cout << sum;
    if(x % sum == 0) answer = true;
    return answer;
}