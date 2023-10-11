#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    
    map<string, int> m1; // m1<선수이름, 등수>
    map<int, string> m2; // m2<등수, 선수이름>
    
    // m1, m2에 초기값 저장
    for(int i = 0; i < players.size(); i++){
        m1[players[i]] = i + 1;
        m2[i + 1] = players[i];
    }
    
    for(int j = 0; j < callings.size(); j++){
        int rank = m1[callings[j]]; // 현재 부른 선수의 등수 저장
        string front = m2[rank - 1]; // 현재 부른 선수의 앞에 있는 선수이름 저장
        
        m1[callings[j]] -= 1; // 현재 부른 선수의 등수-1
        m1[front] += 1; // 앞에 있는 선수 등수+1
        
        m2[rank-1] = callings[j]; // 기존 등수-1에 부른 선수이름 저장
        m2[rank] = front; // 기존 등수에 앞에 있는 선수이름 저장
    }
    
    // answer에 바뀐 순위에 해당하는 선수 이름 삽입
    for(int r = 1; r < players.size() + 1; r++){
        answer.push_back(m2[r]);
    }
    
    return answer;
}