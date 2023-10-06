#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

//k번째 있는 수 반환 함수
int k_num(vector<int> array, vector<int> commands){
    
    //배열 내 인덱스 값에 접근하도록 -1
    int i = commands[0] -1;
    int j = commands[1] -1;
    int k = commands[2] -1;
    
    //i-j까지 자르고 정렬할 벡터
    vector<int> result;
    
    for(int index = i; index <= j; index++){
        result.push_back(array[index]);
    }
    
    //sort
    sort(result.begin(), result.end());
    
    return result[k];
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int i =0; i < commands.size(); i++){
        answer.push_back(k_num(array, commands[i]));
        //cout << k_num(array, commands[i]) << endl;
    }
    
    return answer;
}