#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for(int i = 0; i <= n; i++){
        if(n%i==0){
            if(i%2==1){
                answer++;
            }
        }
    }
    return answer;
}