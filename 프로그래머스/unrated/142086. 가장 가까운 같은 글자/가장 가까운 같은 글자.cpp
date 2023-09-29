#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>


/*
unordered_map은 중복된 데이터를 허용하지 않고 map에 비해 데이터가 많을 시 월등히 좋은 성능을 보입니다.
하지만, key가 유사한 데이터가 많을 시 해시 충돌로 인해 성능이 떨어질 수도 있습니다. */


using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    unordered_map<char, int> umap;
    
    for(int i =0; i < s.length(); i++){
        if(umap.find(s[i]) != umap.end()){ //키가 존재하는 경우
            int index = umap[s[i]];
            answer.push_back(i-index);
            umap[s[i]] = i;
        }else{ //키가 존재하지 않는 경우
            umap[s[i]] = i;
            answer.push_back(-1);
        }
    }
    return answer;
}