#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0;
    int max_height = 0;
    for (auto nametag : sizes){
        int w = max(nametag[0], nametag[1]);
        int h = min(nametag[0], nametag[1]);
        max_width = max(max_width, w);   
        max_height = max(max_height, h);
    }
    return max_width * max_height;
}