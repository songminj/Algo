#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <climits> 

using namespace std;

string solution(string s) {
    stringstream ss(s);
    string temp;
    int num;
    
    int min_val = INT_MAX;
    int max_val = INT_MIN;
    
    while (ss >> num) {
        min_val = min(min_val, num);
        max_val = max(max_val, num);
    }
    
    return to_string(min_val) + " " + to_string(max_val);
}