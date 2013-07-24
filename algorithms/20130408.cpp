#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <cfloat>

using namespace std;

class StarAdventure {
public:
    int memo[60][60][60][60];
    int mostStars( vector <string> level ) {
        int m = (int)level.size();
        int n = (int)level[0].size();
        int res = 0;
        if(m <= 3 || n <= 3) {
            for(int i = 0; i < m; i++) for(int j = 0; j < n; j++) res += level[i][j] - '0';
            return res;
        }
        res = 0;
        memset(memo,0,sizeof(memo));
        for(int i = 0; i < n; i++) for(int j = i+1; j < n; j++) for(int k = j+1; k < n; k++) {
            memo[0][i][j][k] = 0;
            for(int p = 0; p <= k; p++) memo[0][i][j][k] += level[0][p] - '0';
        }
        for(int r = 1; r < m; r++) {
            for(int i = 0; i < n; i++) for(int j = i+1; j < n; j++) for(int k = j+1; k < n; k++) {
                memo[r][i][j][k] = memo[r-1][i][j][k] + level[r][i] - '0' + level[r][j] - '0' + level[r][k] - '0';
            }
            for(int i = 0; i < n; i++) for(int j = i+1; j < n; j++) for(int k = j+1; k < n; k++) {
                if(i-1 >= 0) memo[r][i][j][k] = max(memo[r][i][j][k],memo[r][i-1][j][k] +level[r][i]-'0');
            }
            for(int i = 0; i < n; i++) for(int j = i+1; j < n; j++) for(int k = j+1; k < n; k++) {
                if(j-1 > i) memo[r][i][j][k] = max(memo[r][i][j][k],memo[r][i][j-1][k] +level[r][j]-'0');
            }
            for(int i = 0; i < n; i++) for(int j = i+1; j < n; j++) for(int k = j+1; k < n; k++) {
                if(k-1 > j) memo[r][i][j][k] = max(memo[r][i][j][k],memo[r][i][j][k-1] +level[r][k]-'0');
            }
        }
        return memo[m-1][n-3][n-2][n-1];
    }
};


int main(int argc, char *argv[]) {
        string level[] = {"0123456789", "1123456789", "2223456789", "3333456789", "4444456789", "5555556789", "6666666789", "7777777789", "8888888889", "9999999999"};
        vector<string> test;
        for (int i=0;i<10;i++) {
            test.push_back(level[i]);
        }
        int result = StarAdventure().mostStars(test);
        cout<<result<<endl;
}

