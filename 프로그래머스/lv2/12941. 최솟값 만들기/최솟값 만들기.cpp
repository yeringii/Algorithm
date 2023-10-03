#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int solution(vector<int> a, vector<int> b)
{
    int answer = 0;

    // a 오름차순 정렬, b 내림차순 정렬
    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), greater<int>());
    
    // 계산
    for(int i =0; i < a.size(); i++){
        answer += a[i] * b[i];
    }

    return answer;
}