#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
//stoi를 사용한 비교 -> 문자열의 최대 길이가 10,000이므로 core dump가 뜸
int solution(string t, string p) {
    int answer = 0;
    int p_length = p.length();
    
    for(int i = 0; i <= t.length()-p_length; i++){
        //substr(시작지점, 길이) -> 시작지점부터 길이까지 반환
        string tmp = t.substr(i, p_length);
        
        long tmp_int = stol(tmp);
        long p_int = stol(p);
        
        if(tmp_int <= p_int) answer++;
    }
    return answer;
}