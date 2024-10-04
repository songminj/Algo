#include <string>
#include <stack>
#include <iostream>

using namespace std;

bool check (stack<char>& stack, const string& s) {
        for (char w : s) {
            if (w == '(') {
                stack.push('(');
            } else {
                if(stack.empty()) {
                    return false;
                } else {
                    stack.pop();
            }
        }
    }
    if (stack.empty()) {
        return true;
    } else {
        return false;
    }
}

bool solution(string s)
{
    stack<char> stack;

    return check(stack, s);
}