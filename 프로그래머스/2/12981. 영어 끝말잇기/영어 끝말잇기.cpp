#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    map<string, bool> check;
    int idx =0;
    
    check[words[0]] = true;
    for (int i =1; i < words.size(); i++){
        if(check[words[i]] || words[i].front() != words[i-1].back()) {
            return {(i%n)+1,(i/n)+1};
        }
        check[words[i]] = true;
    }
    
    return {0, 0};
}