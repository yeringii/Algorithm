#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    // 공백, 숫자 toupper, tolower에 영향 안 받음
    answer += toupper(s[0]); // 첫 글자 대문자 만들어줌
    for(int i = 1; i < s.length(); i++){
        if(s[i-1] == ' ') answer += toupper(s[i]); // 공백 뒤에 대문자 만들어줌
        else answer += tolower(s[i]);
    }
    return answer;
}