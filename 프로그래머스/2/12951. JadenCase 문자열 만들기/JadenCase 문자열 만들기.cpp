#include <string>
#include <sstream>
#include <vector>

using namespace std;

string solution(string s) {
    bool isFirst = true;
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ' '){
            isFirst = true;
        } else {
            if (isFirst && isalpha(s[i])){
                s[i] = toupper(s[i]);
            } else {
                s[i] = tolower(s[i]);
            }
            isFirst = false;
        }
    }

    return s;
}