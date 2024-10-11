#include <iostream>
#include <string>
#include <stack>
using namespace std;

int check(string word){
    stack<int> stack;

    for (char c : word){
        if (!stack.empty() && stack.top() == c) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
    return (stack.empty())? 1 : 0;
    
}

int solution(string s) {
    int answer = check(s);
    return answer;
}