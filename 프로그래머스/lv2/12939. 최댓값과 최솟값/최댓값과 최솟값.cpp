#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    
    vector<int> v;
    string tmp;
    //cout << s.length();
    for(int i=0; i<s.length(); i++){
        if(s[i] != ' '){
            //cout << s[i] << '\n';
            tmp += s[i];
        }else{
            // c++ 에서 -도 문자
            // 그래서 -1이면 - 따로 1 따로임
            //cout << tmp << '\n';
            v.push_back(stoi(tmp));
            tmp.clear();
        }
    }
    // 맨 마지막 문자 넣어주기 위해
    v.push_back(stoi(tmp));
    
    // sort 함수 default는 오름차순, vector의 첫번째 원소와 마지막 원소를 answer에 넣어주면 됨
    sort(v.begin(),v.end());
    
    answer += to_string(v.front()) + " " + to_string(v.back());
    
    return answer;
}

